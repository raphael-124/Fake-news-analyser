import requests
import json

payload = {"text": "vaccines contain microchips designed by aliens to track movement.", "model_type": "transformer"}
print("Testing Transformer...")
r = requests.post("http://localhost:8000/api/predict/text", json=payload)
print(f"Status: {r.status_code}")
print(f"Response: {r.text}")
