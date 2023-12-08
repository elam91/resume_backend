from rest_framework.serializers import ModelSerializer

from main.models import PersonalInfo


class PersonalInfoSerializer(ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'
