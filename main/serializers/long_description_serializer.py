from rest_framework.serializers import ModelSerializer

from main.models import LongDescription


class LongDescriptionSerializer(ModelSerializer):
    class Meta:
        model = LongDescription
        fields = '__all__'
