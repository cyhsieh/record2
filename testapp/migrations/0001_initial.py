# Generated by Django 2.0.4 on 2018-04-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testdate', models.DateTimeField(max_length=10, verbose_name='Datetime')),
                ('testmail', models.EmailField(max_length=30, verbose_name='Testmail')),
                ('testtext', models.CharField(blank=True, max_length=20, verbose_name='Testtext')),
            ],
        ),
    ]
