import requests

# Define the API endpoint for importing a zone file
url = 'https://api.nsone.net/v1/import/zone'

# Define your NS1 API key
api_key = 'YOUR_API_KEY_HERE'

# Define the name of the zone you are importing
zone_name = 'example.com'

# Load the zone file data into a variable
with open('example.com.zone', 'r') as file:
    zone_file = file.read()

# Define the payload for the API request
payload = {
    'zone': zone_name,
    'zonefile': zone_file
}

# Define the headers for the API request, including the API key
headers = {
    'X-NSONE-Key': api_key,
    'Content-Type': 'application/json'
}

# Send the API request to import the zone file
response = requests.post(url, headers=headers, json=payload)

# Check the response for errors and handle any errors that occur
if response.status_code == 200:
    print('Zone file imported successfully')
else:
    print('Error importing zone file:', response.text)
