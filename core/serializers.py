from rest_framework import serializers
from .models import Hero, Tag, Subcategory, Footer, FooterSubcategory, Content

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['name', 'href', 'display_name']

class TagSerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = ['category_name', 'subcategories', 'image_url']

class FooterSubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterSubcategory
        fields = ['name', 'url']

class FooterSerializer(serializers.ModelSerializer):
    subcategories = FooterSubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Footer
        fields = ['name', 'subcategories']

class HeroSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    footer = FooterSerializer(many=True, read_only=True)

    class Meta:
        model = Hero
        fields = [
            'id',
            'title', 'description', 'image_url',
            'content_title', 'language', 'tag_title', 'tags',
            'footer', 'website_description'
        ]

class HeroWithLanguageSerializer(serializers.ModelSerializer):
    language_content = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, read_only=True)
    footer = FooterSerializer(many=True, read_only=True)

    class Meta:
        model = Hero
        fields = [
            'id', 'title', 'description', 'image_url',
            'content_title', 'language', 'tag_title', 'tags',
            'footer', 'website_description', 'language_content'
        ]

    def get_language_content(self, obj):
        content = Content.objects.filter(name=obj.language).first()
        if content:
            return ContentSerializer(content).data
        return None

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'