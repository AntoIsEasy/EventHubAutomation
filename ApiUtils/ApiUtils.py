import requests
import uuid


class UtilsAPI:
    def __init__(self):
        self.base_url = "https://api.eventhub.rahulshettyacademy.com/api"

    def get_token(self,email,password):
        payload = {"email":email,"password":password}

        r = requests.post(f"{self.base_url}/auth/login", json=payload, timeout=5)
        if r.status_code != 200:
            raise RuntimeError(f"Login failed: {r.status_code} | body: {r.text}")
        return r.json()["token"]



    def get_ticket_numbers(self,token):
        headers = {"Authorization" : f"Bearer {token}"}

        r = requests.get(f"{self.base_url}/events/285", headers=headers, timeout=5)
        if r.status_code != 200:
            raise RuntimeError(f"Get event failed: {r.status_code} | body: {r.text}")
        return r.json()["data"]["availableSeats"]



    def register_new_user(self):
        credentialis_list=[]
        random_values = uuid.uuid4().hex[:8]
        mail = f"userdemox{random_values}@yopmail.com"
        password = "Userdemo1!"
        credentials = {"email": mail, "password": password}

        r = requests.post(f"{self.base_url}/auth/register", json=credentials, timeout=5)
        if r.status_code != 201:
            raise RuntimeError(f"Registration failed: {r.status_code} | body: {r.text}")
        credentialis_list.append(mail)
        credentialis_list.append(password)

        return credentialis_list


