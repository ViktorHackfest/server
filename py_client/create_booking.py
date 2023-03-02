import requests

endpoint = "http://localhost:8000/travel/bookings/"

data = {
    "tour_guide": "32432242",
    "start_date": "2020-01-01",
    "end_date": "2020-01-02",
    "price": "175000",
    "is_offline": "True",
    "status": "BOOKED",
}

headers = {
    "X-Firebase-ID": "3243224234",
}

response = requests.post(endpoint, data=data, headers=headers)
print(response.json())
