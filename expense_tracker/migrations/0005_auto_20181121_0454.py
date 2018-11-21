# Generated by Django 2.1.3 on 2018-11-21 04:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expense_tracker', '0004_auto_20181121_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 21, 4, 54, 56, 533760, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expense',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]