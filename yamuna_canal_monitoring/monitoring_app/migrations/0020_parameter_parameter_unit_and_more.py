# Generated by Django 4.1.1 on 2022-12-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_app', '0019_remove_site_site_parameter_parameter_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='parameter_unit',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='parameter_unit'),
        ),
        migrations.AlterUniqueTogether(
            name='parameter',
            unique_together={('site', 'parameter_name')},
        ),
    ]
