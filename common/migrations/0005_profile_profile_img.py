# Generated by Django 4.1.3 on 2023-01-08 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_profile_introduce'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='profile_img/'),
        ),
    ]
