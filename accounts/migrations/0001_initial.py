# Generated by Django 2.2.6 on 2020-03-07 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('company_username', models.CharField(default='', max_length=30)),
                ('company_email', models.EmailField(default='', max_length=254)),
                ('category', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TribalYouth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('firstname', models.CharField(max_length=30)),
                ('email', models.EmailField(default='', max_length=254)),
                ('category', models.CharField(default='', max_length=20)),
                ('fullname', models.CharField(default='', max_length=30)),
                ('age', models.IntegerField(default=0)),
                ('highqualification', models.CharField(default='', max_length=20)),
                ('city', models.CharField(default='', max_length=50)),
            ],
        ),
    ]