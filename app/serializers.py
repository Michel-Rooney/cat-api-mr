from rest_framework.serializers import ModelSerializer

from .models import Cat


class CatSerializer(ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'

    def to_representation(self, instance):
        instance.breed = instance.get_breed_display()
        instance.color = instance.get_color_display()
        return super().to_representation(instance)
