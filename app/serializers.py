from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Cat

class CatSerializer(ModelSerializer):
    def get_color_display(self, obj):
        return dict(Cat.CAT_COLOR).get(obj.color)
    
    def get_breed_display(self, obj):
        return dict(Cat.CAT_BREED).get(obj.breed)
    
    color = serializers.SerializerMethodField('get_color_display')
    breed = serializers.SerializerMethodField('get_breed_display')
    
    class Meta:
        model = Cat
        fields = '__all__'


