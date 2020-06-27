from django.db import models

# Create your models here.


class Ml(models.Model):
    PassengerClass = models.CharField(max_length=10000, null=True, blank=True)
    No_siblings = models.CharField(max_length=10000, null=True, blank=True)
    No_children = models.CharField(max_length=10000, null=True, blank=True)
    female = models.CharField(max_length=10000, null=True, blank=True)
    male = models.CharField(max_length=10000, null=True, blank=True)
    result = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.PassengerClass
