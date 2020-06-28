from rest_framework.generics import CreateAPIView
from .apps import MlConfig
from rest_framework.response import Response
from .models import Ml
from .serializer import MlSerializer

# Create your views here.


class MlView(CreateAPIView):
    queryset = Ml.objects.all()
    serializer_class = MlSerializer

    def post(self, request, *args, **kwargs):
        # mldata = MlSerializer(data=request.data)
        # if mldata.is_valid():
        SPassengerClass = request.data['PassengerClass']
        SNo_siblings = request.data['No_siblings']
        SNo_children = request.data['No_children']
        Sfemale = request.data['female']
        Smale = request.data['male']
        PassengerClass = int(request.data['PassengerClass'])
        No_siblings = int(request.data['No_siblings'])
        No_children = int(request.data['No_children'])
        female = int(request.data['female'])
        male = int(request.data['male'])
        res = str(MlConfig.learn(PassengerClass,
                                 No_siblings, No_children, female, male))

        # mldata.result = str(res)
        mldata = Ml.objects.create(PassengerClass=PassengerClass, No_siblings=No_siblings,
                                   No_children=No_children, female=female, male=male, result=res)
        mldata.save()
        return Response(
            {'message': res })
