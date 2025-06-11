from django.db import models

# Create your models here.

class Content(models.Model):
    name = models.TextField()
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
