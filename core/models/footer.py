from django.db import models
from .hero import Hero

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