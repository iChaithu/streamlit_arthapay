import requests

def get_username(url, phone):
    payload = {"phone": phone}
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, {
                "error": f"Request failed with status code {response.status_code}",
                "details": response.text}
    except requests.exceptions.RequestException as e:
        return False, {"error": "Request failed",
                "details": str(e)}
    
def log_in(url, username, password):
    payload = {"username": username,"password": password}
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return True,response.json()
        else:
            return False, {
                "error": f"Request failed with status code {response.status_code}",
                "details": response.text}
    except requests.exceptions.RequestException as e:
        return False, {"error": "Request failed",
                "details": str(e)}