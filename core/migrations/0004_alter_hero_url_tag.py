# Generated by Django 5.2.3 on 2025-06-12 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_hero_url_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='url_tag',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
