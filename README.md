# Custom DNS Resolver with Geolocation

A Python-based application that resolves domain names to IP addresses, fetches geolocation data for those IPs, and visualizes their locations on an interactive map. Built using Streamlit, this tool provides an intuitive interface for networking enthusiasts and developers to explore DNS and geolocation functionalities.
________________________________________
Features
•	DNS Resolution: Converts domain names into their corresponding IP addresses using custom DNS query logic.
•	Geolocation Integration: Fetches geographical details (city, country, latitude, longitude) for resolved IPs using the ipinfo.io API.
•	Interactive Map: Displays IP geolocation on an interactive map with markers using Folium.
•	Dropdown Selection: Allows users to select an IP from resolved addresses and view its location details on the map.
•	Loading Indicators: Displays loading spinners while resolving IPs and generating maps to enhance user experience.
________________________________________
Technologies Used
•	Python: Core programming language.
•	Streamlit: Framework for building the user interface.
•	Folium: Library for creating interactive maps.
•	Requests: For making API calls to fetch geolocation data.
•	Socket and Struct: For custom DNS query and response parsing.
________________________________________
Getting Started
Prerequisites
Ensure you have the following installed:
•	Python 3.7 or higher
•	pip (Python package manager)
Installation
1.	Clone this repository:
2.	git clone https://github.com/your-username/dns-resolver-geolocation.git
3.	cd dns-resolver-geolocation
4.	Install required dependencies:
5.	pip install streamlit requests folium streamlit-folium
6.	Get an API key (optional):
o	For accurate geolocation data, sign up for ipinfo.io and obtain a free API key.
o	Replace the api_url in the get_geolocation function with: 
o	api_url = f"https://ipinfo.io/{ip_address}/json?token=YOUR_API_KEY"
Run the Application
1.	Start the Streamlit server:
2.	streamlit run app.py
________________________________________
How to Use
1.	Enter a domain name (e.g., www.google.com) in the input field.
2.	Click the Resolve button: 
o	The app will fetch all resolved IP addresses for the domain.
o	A dropdown will appear with the list of resolved IPs.
3.	Select an IP from the dropdown: 
o	View its geolocation details (city, country, latitude, longitude).
o	Explore the IP's location on an interactive map.
________________________________________
Project Structure
dns-resolver-geolocation/
│
├── app.py                   # Main Streamlit application
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
________________________________________
Screenshots
DNS Resolution and Geolocation
  ![image](https://github.com/user-attachments/assets/6549c458-08e1-4f07-bf24-326f78fc3f13)

Interactive Map
  ![image](https://github.com/user-attachments/assets/fd544cb5-535e-4c77-ac20-ec59a6bf9e40)

________________________________________
Future Enhancements
•	Support for querying specific DNS record types (e.g., AAAA, MX, CNAME).
•	Batch domain resolution via file upload.
•	Integration of traceroute to visualize network paths.
•	Download feature for results in CSV/JSON format.
•	DNS over HTTPS (DoH) for secure queries.
________________________________________
Contributing
Contributions are welcome! If you have ideas for new features or improvements:
1.	Fork the repository.
2.	Create a new branch: 
3.	git checkout -b feature-name
4.	Commit your changes: 
5.	git commit -m "Add feature-name"
6.	Push to the branch: 
7.	git push origin feature-name
8.	Open a pull request.
________________________________________
License
This project is licensed under the MIT License.
________________________________________
Contact
For questions or feedback, feel free to reach out:
•	Author: Sairaj Dusane
•	Email: sairajdusane@gmail.com
•	LinkedIn: LinkedIn Profile

