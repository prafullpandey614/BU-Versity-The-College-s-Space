# Generated by Django 4.1.3 on 2022-12-12 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("space", "0011_previousyearquestions_pdf_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="previousyearquestions",
            name="subject",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="space.subjects",
            ),
        ),
    ]
