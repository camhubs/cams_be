# Generated by Django 5.2.3 on 2025-06-13 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_model_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='name_url',
        ),
    ]
