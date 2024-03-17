# Generated by Django 4.2.9 on 2024-01-11 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0003_alter_statepopulation_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='indianstates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.TextField(max_length=250)),
                ('population', models.IntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]
