from django.db import models
from .hero import Hero

class Tag(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='tags')
    category_name = models.CharField(max_length=255)
    image_url = models.URLField()

    def __str__(self):
        return self.category_name 