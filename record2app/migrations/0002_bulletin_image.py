# Generated by Django 2.0.1 on 2018-02-28 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record2app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulletin',
            name='image',
            field=models.ImageField(blank=True, max_length=255, upload_to='record2/', verbose_name='Image'),
        ),
    ]
