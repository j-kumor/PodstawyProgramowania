import requests
import json

# Fetch the last 10 Euro exchange rates from the NBP API
url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/last/10/?format=json"
response = requests.get(url)

# Check if the response is successful
if response.status_code == 200:
    data = response.json()  # Get data in JSON format

    # Save the data to euro.json
    with open("euro.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print("Data has been saved to euro.json.")

else:
    print("Error: Unable to fetch data from the NBP API.")
