# Generated by Django 2.2.6 on 2020-03-08 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200308_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribalyouth',
            name='image',
            field=models.ImageField(default='', upload_to='accounts/images'),
        ),
    ]
