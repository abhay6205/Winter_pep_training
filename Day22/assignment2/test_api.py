import requests

url = "http://127.0.0.1:8000/api/students/"

data = {
    "name": "Simplified Student",
    "age": 23,
    "course": "Django"
}

# Send POST request
response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.json())

