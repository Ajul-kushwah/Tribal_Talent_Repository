# Generated by Django 2.2.6 on 2020-03-31 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_tribalyouth_cover_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribalyouth',
            name='cover_photo',
            field=models.ImageField(blank=True, default='media/cover_photo/subscribe-bg.png', null=True, upload_to='cover_photo'),
        ),
    ]
