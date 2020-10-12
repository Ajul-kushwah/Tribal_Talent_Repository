# Generated by Django 2.2.6 on 2020-06-22 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('talent_images', '0008_auto_20200620_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyimages',
            name='desc',
            field=models.TextField(default='###########'),
        ),
        migrations.AddField(
            model_name='companyimages',
            name='title',
            field=models.CharField(default='Image :', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyimages',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(default='', max_length=100)),
                ('other_skill', models.CharField(default='', max_length=100)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
