import requests

def make_api_request(url, phone, password):
    payload = {"phone": phone,"password": password}
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": f"Request failed with status code {response.status_code}",
                "details": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": "Request failed",
                "details": str(e)}

def register_user(url,payload):
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Request failed with status code {response.status_code}","details": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": "Request failed","details": str(e)}