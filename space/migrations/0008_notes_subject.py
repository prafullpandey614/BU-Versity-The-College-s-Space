# Generated by Django 4.1.3 on 2022-12-06 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("space", "0007_remove_branch_semester_alter_notes_pdf_file_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="notes",
            name="subject",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="space.subjects",
            ),
        ),
    ]
