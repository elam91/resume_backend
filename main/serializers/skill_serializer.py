from rest_framework.serializers import ModelSerializer

from main.models import Skill


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
