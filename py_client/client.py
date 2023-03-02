import requests

endpoint = "http://localhost:8000/user/register/?type_user=traveler"

data = {
    "id": "3243224234",
    "uang": "10000100",
}

response = requests.post(endpoint, data=data)
print(response.json())
