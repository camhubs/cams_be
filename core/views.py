from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Hero, Tag, Subcategory, Footer, FooterSubcategory, Content
from .serializers import HeroSerializer, TagSerializer, SubcategorySerializer, FooterSerializer, FooterSubcategorySerializer, ContentSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        hero_data = {
            'title': data.get('hero_title'),
            'description': data.get('hero_description'),
            'image_url': data.get('hero_image_url'),
            'content_title': data.get('content_title'),
            'language': data.get('language'),
            'tag_title': data.get('tag_title'),
            'website_description': data.get('website_description')
        }
        
        hero = Hero.objects.create(**hero_data)
        
        # Create tags
        for tag_data in data.get('tags', []):
            tag = Tag.objects.create(
                hero=hero,
                category_name=tag_data.get('categoryName'),
                image_url=tag_data.get('imageUrl')
            )
            
            # Create subcategories for tag
            for subcategory_data in tag_data.get('subcategories', []):
                Subcategory.objects.create(
                    tag=tag,
                    name=subcategory_data.get('name'),
                    url=subcategory_data.get('url')
                )
        
        # Create footer
        for footer_data in data.get('footer', []):
            footer = Footer.objects.create(
                hero=hero,
                name=footer_data.get('name')
            )
            
            # Create subcategories for footer
            for subcategory_data in footer_data.get('subcategories', []):
                FooterSubcategory.objects.create(
                    footer=footer,
                    name=subcategory_data.get('name'),
                    url=subcategory_data.get('url')
                )
        
        serializer = self.get_serializer(hero)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated]
