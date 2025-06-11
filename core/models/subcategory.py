from django.db import models
from .tag import Tag

class Subcategory(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name 