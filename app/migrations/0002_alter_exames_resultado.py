# Generated by Django 3.2.4 on 2021-06-10 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exames',
            name='resultado',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
