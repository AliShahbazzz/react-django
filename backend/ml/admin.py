from django.contrib import admin
from .models import Ml

@admin.register(Ml)
class FeedbackFormAdmin(admin.ModelAdmin):
    list_display = ['PassengerClass', 'No_siblings', 'No_children']

# Register your models here.
