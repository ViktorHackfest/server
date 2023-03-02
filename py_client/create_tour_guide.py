import requests

endpoint = "http://localhost:8000/user/register/?type_user=tour_guide"

data = {
    "id": "32432242",
    "city": "1"
}

response = requests.post(endpoint, data=data)
print(response.json())
