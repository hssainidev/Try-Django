# Generated by Django 3.2.7 on 2021-09-12 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_article_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='publish',
        ),
    ]
