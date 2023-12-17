from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from main.models import Experience


class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class PDFExperienceSerializer(ModelSerializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    class Meta:
        model = Experience
        fields = '__all__'
