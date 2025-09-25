from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet,add_random_patient,age_chart

router = DefaultRouter()
router.register(r'patients', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add-random/', add_random_patient),
    path('age-chart/', age_chart),
]
