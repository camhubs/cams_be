from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ContentViewSet, HeroViewSet
from .views.page import ModelPageViewSet
from .views.model import ModelViewSet

router = DefaultRouter()
router.register(r'content', ContentViewSet)
router.register(r'hero', HeroViewSet, basename='hero')
router.register(r'model-page', ModelPageViewSet)
router.register(r'model', ModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]