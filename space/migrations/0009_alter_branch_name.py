# Generated by Django 4.1.3 on 2022-12-06 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("space", "0008_notes_subject"),
    ]

    operations = [
        migrations.AlterField(
            model_name="branch",
            name="name",
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]