# Generated by Django 2.2.6 on 2020-03-08 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_tribalyouth_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribalyouth',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='tribalyouth',
            name='firstname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tribalyouth',
            name='highqualification',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='tribalyouth',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]