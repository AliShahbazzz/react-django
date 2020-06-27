from django.urls import path
from .views import MlView

app_name = 'ml'

urlpatterns = [
    path('learn/', MlView.as_view(), name="ml")
]
