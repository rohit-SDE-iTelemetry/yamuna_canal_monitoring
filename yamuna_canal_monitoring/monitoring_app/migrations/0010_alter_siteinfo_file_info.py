# Generated by Django 4.1.1 on 2022-12-14 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_app', '0009_alter_siteinfo_readings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinfo',
            name='file_info',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
