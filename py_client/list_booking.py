import requests

endpoint = "http://localhost:8000/travel/bookings/"

headers = {
    "X-Firebase-ID": "324224234",
}

response = requests.get(endpoint, headers=headers)
print(response.json())
