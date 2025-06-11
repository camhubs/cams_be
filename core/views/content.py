from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from ..models import Content, Hero
from ..serializers import ContentSerializer

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='by-name/(?P<name>[^/.]+)')
    def get_by_name(self, request, name=None):
        content = get_object_or_404(Content, name=name)
        serializer = self.get_serializer(content)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def languages(self, request):
        languages = Hero.objects.values_list('language', flat=True).distinct()
        return Response(list(languages)) 