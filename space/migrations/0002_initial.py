# Generated by Django 4.1.3 on 2023-01-30 16:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import space.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("space", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("headline", models.CharField(max_length=30)),
                ("dp_image", models.ImageField(upload_to=space.utils.ArticlePath)),
                ("update_txt", models.TextField()),
            ],
        ),
      
        migrations.CreateModel(
            name="JobsModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titles", models.CharField(max_length=30)),
                ("date", models.DateField(auto_now_add=True)),
                ("link", models.CharField(max_length=30)),
            ],
        ),
        
      
    ]
