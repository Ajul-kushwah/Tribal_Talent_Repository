# Generated by Django 2.2.6 on 2020-03-23 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20200321_1324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='location',
            new_name='company_trending_name',
        ),
        migrations.AddField(
            model_name='company',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='city_pincode',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='company_status',
            field=models.CharField(default='Active', max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='establishment_year',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='fax_no',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='images',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='company',
            name='landline_no',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='no_of_employee',
            field=models.IntegerField(default=0, max_length=1000),
        ),
        migrations.AddField(
            model_name='company',
            name='registration_no',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='company',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
