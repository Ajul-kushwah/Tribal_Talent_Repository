# Generated by Django 2.2.6 on 2020-03-27 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20200327_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_desc',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
