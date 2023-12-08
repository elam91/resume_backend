from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from main.models import Skill
from main.serializers import SkillSerializer


class SkillView(ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    permission_classes = [AllowAny]
    serializer_class = SkillSerializer