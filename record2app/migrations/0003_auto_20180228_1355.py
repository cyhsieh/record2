# Generated by Django 2.0.1 on 2018-02-28 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record2app', '0002_bulletin_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='image',
            field=models.ImageField(blank=True, max_length=255, upload_to='record2/image/', verbose_name='Image'),
        ),
    ]
