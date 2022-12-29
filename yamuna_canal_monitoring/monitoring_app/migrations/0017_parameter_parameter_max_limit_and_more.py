# Generated by Django 4.1.1 on 2022-12-23 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_app', '0016_remove_reading2022_readingsdict_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='parameter_max_limit',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='parameter_max_limit'),
        ),
        migrations.AddField(
            model_name='parameter',
            name='parameter_min_limit',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='parameter_min_limit'),
        ),
    ]