# Generated by Django 2.2.6 on 2020-03-27 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20200327_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='class_of_company',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_desc',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_trending_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_username',
            field=models.CharField(default='', max_length=100),
        ),
    ]
