# Generated by Django 2.2.6 on 2020-06-19 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent_images', '0003_auto_20200413_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyimages',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]