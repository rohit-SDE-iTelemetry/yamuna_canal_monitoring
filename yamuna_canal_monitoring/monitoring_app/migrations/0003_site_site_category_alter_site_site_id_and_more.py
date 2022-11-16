# Generated by Django 4.1.1 on 2022-11-09 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_app', '0002_site_enable_watsapp_alerts'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='site_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='monitoring_app.category', verbose_name='Site Category'),
        ),
        migrations.AlterField(
            model_name='site',
            name='site_id',
            field=models.CharField(default=None, max_length=80, null=True, unique=True, verbose_name='StationID/SiteID'),
        ),
        migrations.AlterField(
            model_name='site',
            name='user_email',
            field=models.TextField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='Customer Alert Email'),
        ),
        migrations.AlterField(
            model_name='site',
            name='user_phone',
            field=models.TextField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='Customer Alert Contact'),
        ),
    ]