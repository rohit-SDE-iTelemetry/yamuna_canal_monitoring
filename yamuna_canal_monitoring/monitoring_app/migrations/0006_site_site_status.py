# Generated by Django 4.1.1 on 2022-12-14 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_app', '0005_siteinfo_reading2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='site_status',
            field=models.CharField(default='NAT', max_length=20, verbose_name='site status'),
        ),
    ]
