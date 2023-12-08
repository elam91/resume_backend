from rest_framework.serializers import ModelSerializer

from main.models import Social


class SocialSerializer(ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'
