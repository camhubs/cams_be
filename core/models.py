from django.db import models

# Create your models here.

class Content(models.Model):
    name = models.TextField(unique=True)
    href = models.TextField()
    logo_alt = models.TextField()
    logo = models.TextField()
    display_name = models.TextField()
    header_placeholder = models.TextField()
    hero_placeholder = models.TextField()
    hero_button = models.TextField()
    prev = models.TextField()
    next = models.TextField()
    see_more = models.TextField()
    legal_info = models.TextField()

    def __str__(self):
        return self.name

class Hero(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()
    content_title = models.CharField(max_length=255)
    language = models.CharField(max_length=10)
    tag_title = models.CharField(max_length=255)
    website_description = models.TextField()

    def __str__(self):
        return self.title

class Tag(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='tags')
    category_name = models.CharField(max_length=255)
    image_url = models.URLField()

    def __str__(self):
        return self.category_name

class Subcategory(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name

class Footer(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='footer')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class FooterSubcategory(models.Model):
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name
