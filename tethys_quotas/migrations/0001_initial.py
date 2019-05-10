# Generated by Django 2.1.8 on 2019-05-01 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tethys_apps', '0003_python3_compatibility'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EntityQuota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Entity Quota',
            },
        ),
        migrations.CreateModel(
            name='ResourceQuota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, default='', max_length=2048)),
                ('default', models.FloatField()),
                ('units', models.CharField(max_length=100)),
                ('applies_to', models.TextField()),
                ('active', models.BooleanField(default=False)),
                ('impose_default', models.BooleanField(default=True)),
                ('help', models.TextField()),
                ('_handler', models.TextField()),
            ],
            options={
                'verbose_name': 'Resource Quota',
            },
        ),
        migrations.CreateModel(
            name='TethysAppQuota',
            fields=[
                ('entityquota_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tethys_quotas.EntityQuota')),  # noqa: E501
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tethys_apps.TethysApp')),
            ],
            options={
                'verbose_name': 'Tethys App Quota',
            },
            bases=('tethys_quotas.entityquota',),
        ),
        migrations.CreateModel(
            name='UserQuota',
            fields=[
                ('entityquota_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tethys_quotas.EntityQuota')),  # noqa: E501
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Quota',
            },
            bases=('tethys_quotas.entityquota',),
        ),
        migrations.AddField(
            model_name='entityquota',
            name='resource_quota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tethys_quotas.ResourceQuota'),
        ),
    ]