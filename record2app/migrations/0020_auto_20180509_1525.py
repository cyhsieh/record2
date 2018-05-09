# Generated by Django 2.0.4 on 2018-05-09 15:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record2app', '0019_auto_20180429_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=10, verbose_name='姓字')),
                ('sport_item', models.CharField(max_length=20, verbose_name='運動項目')),
                ('sport_date', models.DateField(default=datetime.date(2018, 5, 9), verbose_name='日期')),
            ],
        ),
        migrations.AlterField(
            model_name='record',
            name='purch_date',
            field=models.DateField(default=datetime.date(2018, 5, 9), verbose_name='日期'),
        ),
    ]
