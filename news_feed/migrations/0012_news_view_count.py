# Generated by Django 5.1.6 on 2025-05-16 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_feed', '0011_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
