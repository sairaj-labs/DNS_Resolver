import streamlit as st
import socket
import struct
import requests
import folium
from streamlit_folium import st_folium

# DNS Query Functions
def build_dns_query(domain):
    transaction_id = b'\x00\x01'  # Random transaction ID
    flags = b'\x01\x00'  # Standard query
    qdcount = b'\x00\x01'  # One question
    ancount = b'\x00\x00'  # No answer
    nscount = b'\x00\x00'  # No authority
    arcount = b'\x00\x00'  # No additional

    query_name = b''.join(bytes([len(label)]) + label.encode() for label in domain.split('.'))
    query_name += b'\x00'  # End of the domain name
    query_type = b'\x00\x01'  # Type A (IPv4)
    query_class = b'\x00\x01'  # Class IN (Internet)

    dns_query = transaction_id + flags + qdcount + ancount + nscount + arcount + query_name + query_type + query_class
    return dns_query

def parse_dns_response(response):
    answer_count = struct.unpack("!H", response[6:8])[0]
    answers = []

    offset = 12
    while response[offset] != 0:
        offset += 1
    offset += 5  # Move past QTYPE and QCLASS

    for _ in range(answer_count):
        offset += 10  # Skip Name, Type, Class, TTL
        rdlength = struct.unpack("!H", response[offset:offset + 2])[0]
        offset += 2
        rdata = response[offset:offset + rdlength]
        offset += rdlength
        if rdlength == 4:  # IPv4 address
            ip = ".".join(str(byte) for byte in rdata)
            answers.append(ip)
    return answers

def resolve_domain(domain):
    server = ("8.8.8.8", 53)  # Google Public DNS
    query = build_dns_query(domain)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(5)
        sock.sendto(query, server)
        try:
            response, _ = sock.recvfrom(512)
            return parse_dns_response(response)
        except socket.timeout:
            return ["Error: Timeout while contacting the DNS server."]

# Geolocation Functions
def get_geolocation(ip_address):
    api_url = f"https://ipinfo.io/{ip_address}/json"  # Use ipinfo.io API
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            loc = data.get("loc", None)
            city = data.get("city", "Unknown")
            country = data.get("country", "Unknown")
            return loc, city, country
        else:
            return None, None, None
    except requests.RequestException:
        return None, None, None

def generate_map(latitude, longitude, location_name=""):
    m = folium.Map(location=[latitude, longitude], zoom_start=10)
    folium.Marker(
        location=[latitude, longitude],
        popup=f"Location: {location_name}",
    ).add_to(m)
    return m

# Streamlit App
st.title("Custom DNS Resolver with Geolocation")
st.write("Enter a domain name to resolve its IP addresses and view their geographical locations.")

# Input field
domain = st.text_input("Domain Name", placeholder="e.g., www.youtube.com")

if st.button("Resolve"):
    if domain:
        st.write(f"Resolving domain: `{domain}`")
        with st.spinner("Resolving IP addresses and fetching geolocation data..."):
            ip_addresses = resolve_domain(domain)

            if ip_addresses:
                st.session_state.ip_addresses = ip_addresses  # Save in session state

                # Get geolocation for all resolved IPs
                geo_data = []
                for ip in ip_addresses:
                    loc, city, country = get_geolocation(ip)
                    if loc:
                        latitude, longitude = map(float, loc.split(","))
                        geo_data.append({
                            "ip": ip,
                            "city": city,
                            "country": country,
                            "latitude": latitude,
                            "longitude": longitude
                        })
                    else:
                        geo_data.append({
                            "ip": ip,
                            "city": "Unknown",
                            "country": "Unknown",
                            "latitude": None,
                            "longitude": None
                        })

                st.session_state.geo_data = geo_data  # Save geolocation data in session state
            else:
                st.error("No IP addresses found.")

# Display dropdown and map
if "geo_data" in st.session_state and st.session_state.geo_data:
    geo_data = st.session_state.geo_data

    # Dropdown to select an IP address
    selected_ip = st.selectbox("Select an IP address to view details:", [data["ip"] for data in geo_data])

    # Display details and map for the selected IP
    for data in geo_data:
        if data["ip"] == selected_ip:
            st.write(f"**IP Address**: {data['ip']}")
            st.write(f"**Location**: {data['city']}, {data['country']}")
            if data["latitude"] and data["longitude"]:
                st.write(f"**Coordinates**: {data['latitude']}, {data['longitude']}")
                with st.spinner("Loading map..."):
                    location_map = generate_map(data["latitude"], data["longitude"], f"{data['city']}, {data['country']}")
                    st_folium(location_map, width=700, height=500)
            else:
                st.warning(f"Geolocation not available for IP: {data['ip']}")
