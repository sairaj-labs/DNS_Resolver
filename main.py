from dns_resolver.resolver import Resolver

def main():
    resolver = Resolver()
    domain_name = input("Enter a domain name: ")
    ip_address, location = resolver.resolve(domain_name)

    if "error" in location:
        print("Error fetching location:", location["error"])
    else:
        latitude = float(location["loc"].split(",")[0])
        longitude = float(location["loc"].split(",")[1])
        city = location.get("city", "Unknown")
        country = location.get("country", "Unknown")
        print(f"Domain: {domain_name}")
        print(f"IP Address: {ip_address}")
        print(f"Location: {city}, {country} ({latitude}, {longitude})")
        
        # Generate map
        resolver.geo_locator.generate_map(latitude, longitude, f"{city}, {country}")

if __name__ == "__main__":
    main()
