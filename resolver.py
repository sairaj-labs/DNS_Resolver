from dns_resolver.query_builder import build_query
from dns_resolver.query_sender import send_query
from dns_resolver.response_parser import parse_response
from dns_resolver.geo_locator import GeoLocator

def resolve_dns(domain):
    """Resolves a domain name to its IP addresses and fetches location details."""
    # Step 1: Build the DNS query
    query = build_query(domain)
    
    # Step 2: Send the query to get the response
    response = send_query(query)
    
    # Step 3: Parse the DNS response to extract IP addresses
    answers = parse_response(response)
    
    if not answers:
        print(f"No IP addresses found for {domain}.")
        return None
    
    print(f"Resolved IP addresses for {domain}: {answers}")
    
    # Step 4: Get the location of the first IP address
    geo_locator = GeoLocator(api_url="https://ipinfo.io")  # Use your chosen API URL
    ip_address = answers[0]  # Take the first resolved IP address
    location = geo_locator.get_location(ip_address)
    
    if "error" in location:
        print(f"Error fetching location for {ip_address}: {location['error']}")
        return answers

    # Step 5: Extract latitude and longitude from the location data
    latitude, longitude = map(float, location["loc"].split(","))
    city = location.get("city", "Unknown")
    country = location.get("country", "Unknown")
    
    print(f"Geolocation for IP {ip_address}: {city}, {country} ({latitude}, {longitude})")
    
    # Step 6: Generate a map for the IP address
    geo_locator.generate_map(latitude, longitude, f"{city}, {country}")
    
    return answers
