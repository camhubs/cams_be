from django.db import models

class ModelPage(models.Model):
    tag = models.CharField(max_length=255, unique=True)
    home_name = models.CharField(max_length=255)
    likes = models.CharField(max_length=255)
    hottest = models.CharField(max_length=255)
    last_updated = models.CharField(max_length=255)
    status_online = models.CharField(max_length=255)
    status_offline = models.CharField(max_length=255)
    check_schedule = models.CharField(max_length=255)
    check_bio = models.CharField(max_length=255)
    herp_image = models.CharField(max_length=255)
    about_model = models.CharField(max_length=255)
    model_statistics = models.CharField(max_length=255)
    related_cams = models.CharField(max_length=255)
    sign_up_here = models.CharField(max_length=255)
    sign_up_description = models.TextField()
    popular_times = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    monday = models.CharField(max_length=255)
    tuesday = models.CharField(max_length=255)
    wednesday = models.CharField(max_length=255)
    thursday = models.CharField(max_length=255)
    friday = models.CharField(max_length=255)
    saturday = models.CharField(max_length=255)
    sunday = models.CharField(max_length=255)
    footer_button_title = models.CharField(max_length=255)
    footer_button = models.CharField(max_length=255)

    def __str__(self):
        return self.tag 