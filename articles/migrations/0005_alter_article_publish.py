# Generated by Django 3.2.7 on 2021-09-12 17:30

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('articles', '0004_article_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(blank=True,
                                       default=datetime.datetime(2021, 9, 12, 17, 30, 52, 221111, tzinfo=utc),
                                       null=True),
        ),
    ]
