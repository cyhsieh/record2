# Generated by Django 2.0.4 on 2018-04-29 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record2app', '0017_auto_20180428_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='purch_date',
            field=models.DateField(default=datetime.date(2018, 4, 29), verbose_name='日期'),
        ),
    ]