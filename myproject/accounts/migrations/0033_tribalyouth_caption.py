# Generated by Django 2.2.6 on 2020-10-07 19:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_auto_20200806_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribalyouth',
            name='caption',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]