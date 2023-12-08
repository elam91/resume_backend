from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from main.models import LongDescription
from main.serializers import LongDescriptionSerializer


class LongDescriptionView(ReadOnlyModelViewSet):
    queryset = LongDescription.objects.all()
    permission_classes = [AllowAny]
    serializer_class = LongDescriptionSerializer