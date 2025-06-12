from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import ModelPage
from ..serializers import ModelPageSerializer

class ModelPageViewSet(viewsets.ModelViewSet):
    queryset = ModelPage.objects.all()
    serializer_class = ModelPageSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='by-tag/(?P<tag>[^/.]+)')
    def get_by_tag(self, request, tag=None):
        model_page = get_object_or_404(ModelPage, tag=tag)
        serializer = self.get_serializer(model_page)
        return Response(serializer.data) 