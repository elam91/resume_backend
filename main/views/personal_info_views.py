from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from main.models import PersonalInfo
from main.serializers import PersonalInfoSerializer


class PersonalInfoView(ReadOnlyModelViewSet):
    queryset = PersonalInfo.objects.order_by("-created_at").first()
    permission_classes = [AllowAny]
    serializer_class = PersonalInfoSerializer