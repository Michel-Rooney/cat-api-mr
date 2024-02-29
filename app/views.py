from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CatSerializer
from .models import Cat


class CatViewSets(ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    @action(['GET'], False)
    def get_color(self, response):
        return Response(Cat.CAT_COLOR)
    
    
    @action(['GET'], False)
    def get_breed(self, response):
        return Response(Cat.CAT_BREED)