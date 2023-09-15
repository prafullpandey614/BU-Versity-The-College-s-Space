# Generated by Django 3.2.6 on 2021-09-01 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_clubsociety_president'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='clubsociety',
            name='President',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
