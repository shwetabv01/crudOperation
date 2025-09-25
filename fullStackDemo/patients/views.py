from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
import requests
import matplotlib.pyplot as plt
import io
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

@api_view(["POST"])
def add_random_patient(request):
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

    return JsonResponse({
        "message": "Patient added from external API",
        "patient": {
            "id": patient.id,
            "first_name": patient.first_name,
            "last_name": patient.last_name,
            "email": patient.email
        }
    })


def age_chart(request):
    ages = [p.age for p in Patient.objects.all()]

    plt.figure(figsize=(6, 4))
    plt.hist(ages, bins=10, color="skyblue")
    plt.title("Patient Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    return HttpResponse(buf.getvalue(), content_type="image/png")