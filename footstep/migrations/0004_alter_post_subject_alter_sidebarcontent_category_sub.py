# Generated by Django 4.1.3 on 2022-12-03 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footstep', '0003_post_modify_date_alter_post_category_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subject',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='sidebarcontent',
            name='category_sub',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
