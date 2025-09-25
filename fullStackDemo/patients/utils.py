import requests
from .models import Patient

def fetch_random_user():
    response = requests.get("https://randomuser.me/api/")
    data = response.json()['results'][0]

    patient = Patient.objects.create(
        first_name=data['name']['first'],
        last_name=data['name']['last'],
        age=data['dob']['age'],
        gender=data['gender'],
        email=data['email'],
        phone=data['phone'],
        address=f"{data['location']['street']['number']} {data['location']['street']['name']}, {data['location']['city']}"
    )
    return patient
