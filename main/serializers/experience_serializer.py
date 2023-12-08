from rest_framework.serializers import ModelSerializer

from main.models import Experience


class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
