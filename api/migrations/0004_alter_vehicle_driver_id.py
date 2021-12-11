# Generated by Django 3.2.9 on 2021-12-08 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_vehicle_plate_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='driver_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='api.driver'),
        ),
    ]