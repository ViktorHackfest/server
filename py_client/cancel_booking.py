import requests

endpoint = "http://localhost:8000/travel/bookings/5/"

data = {
    "status": "CANCELLED",
}

headers = {
    "X-Firebase-ID": "3243224234",
}

response = requests.patch(endpoint, data=data, headers=headers)
print(response.json())
