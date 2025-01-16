import requests
import folium
class GeoLocator:
    def __init__(self, api_url, api_key=None):
        self.api_url ="http://api.ipstack.com"
        self.api_key ="18e51804a7ab5214a0d1c3cced942995"

    def get_location(self, ip_address):
        params = {"access_key": self.api_key, "ip": ip_address} if self.api_key else {}
        response = requests.get(f"{self.api_url}/{ip_address}", params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Unable to fetch location"}
    def generate_map(self, latitude, longitude, location_name=""):
        m = folium.Map(location=[latitude, longitude], zoom_start=10)
        folium.Marker(
            location=[latitude, longitude],
            popup=f"Location: {location_name}",
        ).add_to(m)
        m.save("location_map.html")
        print("Map saved as location_map.html")