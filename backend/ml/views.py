from rest_framework.generics import CreateAPIView
from .apps import MlConfig
from rest_framework.response import Response
from .models import Ml
from .serializer import MlSerializer

# Create your views here.


class Ml(CreateAPIView):
    queryset = Ml.objects.all()
    serializer_class = MlSerializer

    def post(self, request):
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

        mldata = MlSerializer(data=request.data)
        if mldata.is_valid():
            mldata.save(result=res)
            return Response(
                {'message': res})
        return Response(
            {'message': mldata.errors})
