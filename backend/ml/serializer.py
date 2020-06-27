from rest_framework import serializers

from .models import Ml


class MlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ml
        fields = '__all__'
