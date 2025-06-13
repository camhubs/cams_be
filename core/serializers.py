from rest_framework import serializers
from .models import Hero, Tag, Subcategory, Footer, FooterSubcategory, Content, ModelPage, Model, ModelStatistic, ModelTag

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
            'id', 'title', 'description', 'image_url',
            'content_title', 'language', 'tag_title', 'url_tag',
            'tags', 'footer', 'website_description'
        ]

class HeroWithLanguageSerializer(serializers.ModelSerializer):
    language_content = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, read_only=True)
    footer = FooterSerializer(many=True, read_only=True)

    class Meta:
        model = Hero
        fields = [
            'id', 'title', 'description', 'image_url',
            'content_title', 'language', 'tag_title', 'url_tag',
            'tags', 'footer', 'website_description', 'language_content'
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

class ModelPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelPage
        fields = '__all__'

class ModelStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelStatistic
        fields = ['name', 'value']

class ModelTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelTag
        fields = ['tag', 'tag_name']
class ModelSerializer(serializers.ModelSerializer):
    statistics = ModelStatisticSerializer(many=True)
    tags = ModelTagSerializer(many=True)

    class Meta:
        model = Model
        fields = [
            'id', 'nikname', 'name', 'about_model',
            'statistics', 'tags', 'footer_button_url',
            'sign_up_here_url', 'popular_times', 'hero_url',
            'last_updated', "avatar"
        ]

    def create(self, validated_data):
        statistics_data = validated_data.pop('statistics', [])
        tags_data = validated_data.pop('tags', [])

        model = Model.objects.create(**validated_data)

        for stat_data in statistics_data:
            ModelStatistic.objects.create(model=model, **stat_data)

        for tag_data in tags_data:
            ModelTag.objects.create(model=model, **tag_data)

        return model

    def update(self, instance, validated_data):
        statistics_data = validated_data.pop('statistics', [])
        tags_data = validated_data.pop('tags', [])

        # Update main fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update statistics
        instance.statistics.all().delete()
        for stat_data in statistics_data:
            ModelStatistic.objects.create(model=instance, **stat_data)

        # Update tags
        instance.tags.all().delete()
        for tag_data in tags_data:
            ModelTag.objects.create(model=instance, **tag_data)

        return instance