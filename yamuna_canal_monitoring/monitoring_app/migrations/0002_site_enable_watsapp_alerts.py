# Generated by Django 4.1.1 on 2022-11-09 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='enable_watsapp_alerts',
            field=models.BooleanField(blank=True, default=False, help_text='send sms alerts', verbose_name='Watsapp Alerts'),
        ),
    ]
