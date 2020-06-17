from django.urls import path
from . import views

app_name = 'contactform'

urlpatterns = [
    path('contact/', views.ContactAPIView.as_view(), name="contact"),
]
