from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from main.models import Experience
from main.serializers import ExperienceSerializer


class ExperienceView(ReadOnlyModelViewSet):
    queryset = Experience.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ExperienceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['experience_type']