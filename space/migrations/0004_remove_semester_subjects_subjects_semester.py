# Generated by Django 4.1.3 on 2022-12-06 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("space", "0003_alter_semester_subjects"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="semester",
            name="subjects",
        ),
        migrations.AddField(
            model_name="subjects",
            name="semester",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="space.semester",
            ),
        ),
    ]