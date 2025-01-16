import socket

def send_query(query, server="8.8.8.8", port=53):
    """Sends a DNS query to the specified server and returns the response."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(5)  # Set timeout to 5 seconds
        sock.sendto(query, (server, port))
        response, _ = sock.recvfrom(512)
        sock.close()
        print(f"Received response: {response}")
        return response
    except socket.timeout:
        print("DNS query timed out.")
        return None
