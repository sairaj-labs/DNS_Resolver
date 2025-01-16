import struct

def build_query(domain):
    """Builds a DNS query packet for the given domain."""
    header = struct.pack(">HHHHHH", 12345, 0x0100, 1, 0, 0, 0)
    qname = b"".join(struct.pack("B", len(part)) + part.encode() for part in domain.split("."))
    qname += b'\0'
    question = qname + struct.pack(">HH", 1, 1)

    print(f"Built DNS Query for {domain}: {header + question}")
    return header + question
