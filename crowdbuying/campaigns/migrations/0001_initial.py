# Generated by Django 2.1.7 on 2019-03-04 04:00

import campaigns.models
import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('duration', models.DurationField(verbose_name=datetime.timedelta(days=30))),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, default='Campaign description...', max_length=255)),
                ('discount', models.IntegerField(default=0)),
                ('numbermembers', models.IntegerField(default=0)),
                ('slug', models.IntegerField(default=campaigns.models.Campaign.random_code, unique=True)),
                ('members', models.ManyToManyField(related_name='membership', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
