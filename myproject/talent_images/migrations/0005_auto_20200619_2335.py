# Generated by Django 2.2.6 on 2020-06-19 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent_images', '0004_auto_20200619_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimages',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
