from django.urls import re_path
from rest_framework.routers import DefaultRouter
from .views import VehicleViewset, generate_report

router = DefaultRouter()
router.register(r'vehicle', VehicleViewset, basename='vehicle')
repor_url = [re_path(r'repor/(?P<email>.*)', generate_report, name='report')]

urlpatterns = router.urls + repor_url
