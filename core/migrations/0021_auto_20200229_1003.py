# Generated by Django 3.0 on 2020-02-29 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20200229_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='Property/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='property',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='Property/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='property',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='Property/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='property',
            name='photo_4',
            field=models.ImageField(blank=True, upload_to='Property/%Y/%m/%d'),
        ),
    ]
