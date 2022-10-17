# Generated by Django 2.2 on 2022-05-19 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20220515_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salononsitebooking',
            name='cancellation_reason',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='cancellation_reasons_bookings', to='main_app.CancellationReason'),
        ),
    ]