# Generated by Django 4.2.9 on 2024-01-11 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statepopulation',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='statepopulation',
            name='longitude',
            field=models.FloatField(),
        ),
    ]