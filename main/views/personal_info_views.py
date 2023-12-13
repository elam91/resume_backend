from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from main.models import PersonalInfo
from main.serializers import PersonalInfoSerializer


class PersonalInfoView(ReadOnlyModelViewSet):
    queryset = PersonalInfo.objects.order_by("-created_at").all()
    permission_classes = [AllowAny]
    serializer_class = PersonalInfoSerializer

    @extend_schema(responses=PersonalInfoSerializer)
    @action(methods=["GET"], detail=False, permission_classes=[AllowAny])
    def latest(self, request, pk=None):
        queryset = self.get_queryset()
        latest = queryset.first()
        serializer = self.get_serializer(latest)
        return Response(serializer.data)
