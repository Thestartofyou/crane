
import requests
import json

def get_crane_permits(api_key):
    base_url = "https://data.cityofnewyork.us/resource/hp2j-jikz.json"
    params = {"$limit": 10, "permit_type_description": "CONSTRUCTION CRANE"}
    headers = {"X-App-Token": api_key}

    response = requests.get(base_url, params=params, headers=headers)
    if response.status_code == 200:
        crane_permits = response.json()
        return crane_permits
    else:
        print(f"Failed to retrieve crane permits data. Status code: {response.status_code}")
        return None

def main():
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = 'YOUR_API_KEY'

    crane_permits = get_crane_permits(api_key)
    if crane_permits:
        print(json.dumps(crane_permits, indent=2))

if __name__ == "__main__":
    main()
