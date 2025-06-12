from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Model
from ..serializers import ModelSerializer

class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='by-name-url/(?P<name_url>[^/.]+)')
    def get_by_name_url(self, request, name_url=None):
        model = get_object_or_404(Model, name_url=name_url)
        serializer = self.get_serializer(model)
        return Response(serializer.data) 