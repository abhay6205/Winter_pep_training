import requests

url = "http://127.0.0.1:8000/api/students/"

data = {
    "name": "Serializer Student",
    "age": 21,
    "course": "CSE"
}

# POST
response = requests.post(url, json=data)
print("POST Response:", response.json())

# GET
response = requests.get(url)
print("GET Response:", response.json())
