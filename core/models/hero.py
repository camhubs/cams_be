from django.db import models

class Hero(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()
    content_title = models.CharField(max_length=255)
    language = models.CharField(max_length=10)
    tag_title = models.CharField(max_length=255)
    url_tag = models.CharField(max_length=255, unique=True)
    website_description = models.TextField()

    def __str__(self):
        return self.title 