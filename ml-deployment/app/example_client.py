import requests

API_URL = 'http://localhost:8000/predict'

payload = {
    "features": {
        "age": 30,
        "income": 45000
    }
}

resp = requests.post(API_URL, json=payload)
print('status', resp.status_code)
print(resp.json())
