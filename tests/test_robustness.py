import requests

BASE_URL = "http://localhost:8000/api"

def test_url(url, model_type="logistic"):
    payload = {"url": url, "model_type": model_type}
    try:
        print(f"Testing URL: {url} ...")
        response = requests.post(f"{BASE_URL}/predict/url", json=payload)
        if response.status_code == 200:
            print(f"SUCCESS: {response.json().get('prediction')}")
        else:
            print(f"EXPECTED ERROR {response.status_code}: {response.json().get('detail')}")
    except Exception as e:
        print(f"Request failed: {e}")

def test_text(text, model_type="logistic"):
    payload = {"text": text, "model_type": model_type}
    try:
        print(f"Testing Empty Text ...")
        response = requests.post(f"{BASE_URL}/predict/text", json=payload)
        if response.status_code == 200:
            print(f"SUCCESS: {response.json().get('prediction')}")
        else:
            print(f"EXPECTED ERROR {response.status_code}: {response.json().get('detail')}")
    except Exception as e:
        print(f"Request failed: {e}")

print("--- Robustness Tests ---")
# 1. Invalid URL
test_url("https://this-domain-does-not-exist-12345.com")

# 2. Non-HTML content (image)
test_url("https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png")

# 3. Empty text
test_text("   ")

# 4. Valid URL (Google - though it might block scraping if robot detection is strong, we just test the flow)
test_url("https://www.google.com")
