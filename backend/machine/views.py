from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Machine
from .serializers import MachineSerializer
from rest_framework.response import Response
# Create your views here.


class Machine(CreateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    def post(self, request):
        machineData = MachineSerializer(data=request.data)
        if machineData.is_valid():
            data = machineData.save()
            machineData = MachineSerializer(data).data['result']
            return Response({
                'message': machineData
            })
