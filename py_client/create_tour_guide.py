import requests

endpoint = "http://localhost:8000/user/register/?type_user=tour_guide"

data = {
    "id": "3243224",
    "city": "1",
    "name": "Nguyen Van A",
    "photo_url": "https://www.google.com",
}

response = requests.post(endpoint, data=data)
print(response.json())
