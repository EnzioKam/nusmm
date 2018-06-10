# Generated by Django 2.0.6 on 2018-06-03 15:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapping',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 6, 3, 15, 46, 45, 365514, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mapping',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]