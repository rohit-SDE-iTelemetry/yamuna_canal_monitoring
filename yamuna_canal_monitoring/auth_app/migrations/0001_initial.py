# Generated by Django 4.1.1 on 2022-09-20 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('monitoring_app', '0002_remove_site_created_at_remove_site_last_updated_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('email', models.EmailField(default=None, max_length=60, null=True, unique=True)),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('phone', models.CharField(max_length=10, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('last_pwd_updated', models.DateField(auto_now=True, verbose_name='Password Updated On')),
                ('user_type', models.CharField(choices=[('CUSTOMER', 'Customer'), ('CPCB', 'CPCB'), ('ADMIN', 'Super Admin'), ('STAFF', 'Staff User')], max_length=20)),
                ('on_trial', models.BooleanField(default=False)),
                ('address', models.TextField(default=None, null=True)),
                ('zipcode', models.IntegerField(default=None, null=True)),
                ('state', models.CharField(max_length=80, null=True)),
                ('city', models.CharField(max_length=80, null=True)),
                ('country', models.CharField(default='India', editable=False, max_length=80)),
                ('permissions', models.ManyToManyField(default=None, to='auth.permission')),
                ('site', models.ManyToManyField(default=None, to='monitoring_app.site')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
