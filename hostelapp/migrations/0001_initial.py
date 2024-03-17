# Generated by Django 4.2.9 on 2024-01-11 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_number', models.IntegerField()),
                ('is_occupied', models.BooleanField(default=False)),
                ('status', models.CharField(default='active', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EVChargingLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=250)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_number', models.IntegerField()),
                ('number_of_rooms', models.IntegerField(null=True)),
                ('status', models.CharField(default='active', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('organisation', models.CharField(default='Default Organisation', max_length=100)),
                ('branch', models.CharField(default='Default Branch', max_length=100)),
                ('total_floors', models.IntegerField(blank=True, null=True)),
                ('total_rooms', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(default='active', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=10)),
                ('capacity', models.IntegerField(null=True)),
                ('max_occupancy', models.IntegerField(null=True)),
                ('number_of_beds', models.IntegerField(default=0, null=True)),
                ('status', models.CharField(default='active', max_length=20)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostelapp.floor')),
            ],
        ),
        migrations.CreateModel(
            name='StatePopulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=250)),
                ('population', models.IntegerField()),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('organisation', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='active', max_length=20)),
                ('admission_date', models.DateField(blank=True, null=True)),
                ('bed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostelapp.bed')),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostelapp.floor')),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostelapp.hostel')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostelapp.room')),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hostelapp.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='HostelStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_floors', models.IntegerField()),
                ('total_rooms', models.IntegerField()),
                ('hostel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hostelapp.hostel')),
            ],
        ),
        migrations.AddField(
            model_name='floor',
            name='hostel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostelapp.hostel'),
        ),
        migrations.AddField(
            model_name='bed',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostelapp.room'),
        ),
    ]
