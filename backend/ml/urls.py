from django.urls import path
from .views import Ml

app_name = 'ml'

urlpatterns = [
    path('learn/', Ml.as_view(), name="ml")
]
