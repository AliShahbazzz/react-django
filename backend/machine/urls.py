from django.urls import path
from . import views

app_name = 'machine'

urlpatterns = [
    path('learning/', views.Machine.as_view(), name="machine")
]
