from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import ModelPage
from ..serializers import ModelPageSerializer

class ModelPageViewSet(viewsets.ModelViewSet):
    queryset = ModelPage.objects.all()
    serializer_class = ModelPageSerializer
    permission_classes = [IsAuthenticated] 