import struct

def parse_response(response):
    """Parses the DNS response and extracts the IP addresses."""
    if not response:
        print("No response received.")
        return []

    # Header is 12 bytes, question section follows
    header_size = 12
    question_end = response.find(b'\0', header_size) + 5  # End of question section
    answer_start = question_end

    answers = []
    while answer_start < len(response):
        # Skip Name (2 bytes if compressed, otherwise variable length)
        if response[answer_start] & 0xC0 == 0xC0:
            answer_start += 2  # Compressed name
        else:
            while response[answer_start] != 0:
                answer_start += 1 + response[answer_start]
            answer_start += 1

        # Read Type, Class, TTL, Data Length
        answer_start += 2  # Type
        answer_start += 2  # Class
        answer_start += 4  # TTL
        data_length = struct.unpack(">H", response[answer_start:answer_start + 2])[0]
        answer_start += 2  # Data Length

        # If Type is A (IPv4) and Data Length is 4
        if data_length == 4:
            ip = ".".join(map(str, response[answer_start:answer_start + data_length]))
            answers.append(ip)

        # Move to the next record
        answer_start += data_length

    return answers
