from django.db import models

class Model(models.Model):
    nikname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    about_model = models.TextField()
    footer_button_url = models.CharField(max_length=255)
    sign_up_here_url = models.CharField(max_length=255)
    hero_url = models.CharField(max_length=255)
    last_updated = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255, default='')
    def __str__(self):
        return self.name

class ModelStatistic(models.Model):
    model = models.ForeignKey(Model, related_name='statistics', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}: {self.value}"

class ModelTag(models.Model):
    model = models.ForeignKey(Model, related_name='tags', on_delete=models.CASCADE)
    tag = models.CharField(max_length=255)
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name

class ModelPopularTime(models.Model):
    model = models.ForeignKey(Model, related_name='popular_times', on_delete=models.CASCADE)
    day = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.day} {self.time}" 