from django.db import models
from .tag import Tag

class Subcategory(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=255)
    href = models.CharField(max_length=255, blank=True)
    display_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name 