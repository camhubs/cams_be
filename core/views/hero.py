from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from ..models import Hero, Tag, Subcategory, Footer, FooterSubcategory
from ..serializers import HeroSerializer, HeroWithLanguageSerializer

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve_by_url_tag':
            return HeroWithLanguageSerializer
        return self.serializer_class

    @action(detail=False, methods=['get'], url_path='by-url-tag/(?P<url_tag>[^/.]+)', permission_classes=[AllowAny])
    def retrieve_by_url_tag(self, request, url_tag=None):
        hero = get_object_or_404(Hero, url_tag=url_tag)
        serializer = self.get_serializer(hero)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        hero_data = {
            'title': data.get('title'),
            'description': data.get('description'),
            'image_url': data.get('image_url'),
            'content_title': data.get('content_title'),
            'language': data.get('language'),
            'tag_title': data.get('tag_title'),
            'url_tag': data.get('url_tag'),
            'website_description': data.get('website_description')
        }
        
        hero = Hero.objects.create(**hero_data)
        
        # Create tags
        for tag_data in data.get('tags', []):
            tag = Tag.objects.create(
                hero=hero,
                category_name=tag_data.get('category_name'),
                image_url=tag_data.get('image_url')
            )
            
            # Create subcategories for tag
            for subcategory_data in tag_data.get('subcategories', []):
                Subcategory.objects.create(
                    tag=tag,
                    name=subcategory_data.get('name'),
                    href=subcategory_data.get('href'),
                    display_name=subcategory_data.get('display_name')
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

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data

        # Update Hero fields
        instance.title = data.get('title', instance.title)
        instance.description = data.get('description', instance.description)
        instance.image_url = data.get('image_url', instance.image_url)
        instance.content_title = data.get('content_title', instance.content_title)
        instance.language = data.get('language', instance.language)
        instance.tag_title = data.get('tag_title', instance.tag_title)
        instance.url_tag = data.get('url_tag', instance.url_tag)
        instance.website_description = data.get('website_description', instance.website_description)
        instance.save()

        # Update tags
        if 'tags' in data:
            # Delete existing tags
            instance.tags.all().delete()
            # Create new tags
            for tag_data in data['tags']:
                tag = Tag.objects.create(
                    hero=instance,
                    category_name=tag_data.get('category_name'),
                    image_url=tag_data.get('image_url')
                )
                # Create subcategories for tag
                for subcategory_data in tag_data.get('subcategories', []):
                    Subcategory.objects.create(
                        tag=tag,
                        name=subcategory_data.get('name'),
                        href=subcategory_data.get('href'),
                        display_name=subcategory_data.get('display_name')
                    )

        # Update footer
        if 'footer' in data:
            # Delete existing footer
            instance.footer.all().delete()
            # Create new footer
            for footer_data in data['footer']:
                footer = Footer.objects.create(
                    hero=instance,
                    name=footer_data.get('name')
                )
                # Create subcategories for footer
                for subcategory_data in footer_data.get('subcategories', []):
                    FooterSubcategory.objects.create(
                        footer=footer,
                        name=subcategory_data.get('name'),
                        url=subcategory_data.get('url')
                    )

        serializer = self.get_serializer(instance)
        return Response(serializer.data) 