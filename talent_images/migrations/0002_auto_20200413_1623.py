# Generated by Django 2.2.6 on 2020-04-13 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent_images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimages',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]