# Generated by Django 2.0.4 on 2018-04-15 16:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record2app', '0010_auto_20180407_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='purch_date',
            field=models.DateField(default=datetime.date(2018, 4, 15), verbose_name='日期'),
        ),
    ]