from drf_spectacular.utils import  extend_schema, OpenApiParameter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from main.models import LongDescription
from main.serializers import LongDescriptionSerializer


class LongDescriptionView(ReadOnlyModelViewSet):
    queryset = LongDescription.objects.all()
    permission_classes = [AllowAny]
    serializer_class = LongDescriptionSerializer

    lookup_url_kwarg = 'page'
    lookup_field = 'page'


    def retrieve(self, request, *args, **kwargs):
        instance = self.queryset.get(page=kwargs.get('page'))
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
