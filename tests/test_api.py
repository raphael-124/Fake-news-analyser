import requests

BASE_URL = "http://localhost:8000/api"

def test_model(model_type):
    payload = {"text": "vaccines contain microchips designed by aliens to track movement.", "model_type": model_type}
    try:
        response = requests.post(f"{BASE_URL}/predict/text", json=payload)
        if response.status_code == 200:
            print(f"Response: {response.json()}")
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Request failed: {e}")

print("Testing Logistic Regression...")
test_model("logistic")

print("\nTesting Random Forest...")
test_model("random_forest")

print("\nTesting Transformer...")
test_model("transformer")
