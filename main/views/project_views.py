from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from main.models import Project
from main.serializers import ProjectSerializer


class ProjectView(ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ProjectSerializer