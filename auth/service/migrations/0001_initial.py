# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-04 00:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time', models.DateTimeField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('edit_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('state', models.IntegerField(choices=[(0, 'AL'), (1, 'AB')])),
                ('city', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=30)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('size', models.IntegerField()),
                ('tz', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time', models.DateTimeField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('edit_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('introduction', models.TextField()),
                ('org_type', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RegisterKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time', models.DateTimeField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('edit_time', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=100)),
                ('role', models.IntegerField()),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stakeholder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delete_time', models.DateTimeField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('edit_time', models.DateTimeField(auto_now=True)),
                ('nick_name', models.CharField(max_length=100)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('role', models.IntegerField()),
                ('tz', models.CharField(max_length=10)),
                ('lang', models.CharField(max_length=10)),
                ('django_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('home', models.ManyToManyField(to='service.Home')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
