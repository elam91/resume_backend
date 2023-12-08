from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from main.models import Social
from main.serializers import SocialSerializer


class SocialView(ReadOnlyModelViewSet):
    queryset = Social.objects.all()
    permission_classes = [AllowAny]
    serializer_class = SocialSerializer