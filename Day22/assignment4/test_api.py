import requests

url = "http://127.0.0.1:8000/api/students/"

# 1. Valid Student
valid_data = {
    "name": "Valid Student",
    "age": 20,
    "course": "IT"
}
print("Testing Valid Data...")
response = requests.post(url, json=valid_data)
print("Status:", response.status_code)
print("Response:", response.json())
print("-" * 30)

# 2. Invalid Student (Age < 5)
invalid_data = {
    "name": "Invalid Student",
    "age": 3,
    "course": "IT"
}
print("Testing Invalid Data (Age < 5)...")
response = requests.post(url, json=invalid_data)
print("Status:", response.status_code)
print("Response:", response.json())
