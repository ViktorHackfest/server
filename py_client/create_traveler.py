import requests

endpoint = "http://localhost:8000/user/register/?type_user=traveler"

data = {
    "id": "324224234",
    "money": "10000100",
}

response = requests.post(endpoint, data=data)
print(response.json())
