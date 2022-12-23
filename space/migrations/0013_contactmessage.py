# Generated by Django 4.1.3 on 2022-12-12 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("space", "0012_previousyearquestions_subject"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactMessage",
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
                ("name", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=20)),
                ("message", models.TextField()),
            ],
        ),
    ]