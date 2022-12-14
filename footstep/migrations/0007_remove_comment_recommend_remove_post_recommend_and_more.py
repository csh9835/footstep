# Generated by Django 4.1.3 on 2022-12-13 15:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('footstep', '0006_comment_recommend_post_recommend_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='recommend',
        ),
        migrations.RemoveField(
            model_name='post',
            name='recommend',
        ),
        migrations.AddField(
            model_name='comment',
            name='recommend',
            field=models.ManyToManyField(related_name='recommend_comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='recommend',
            field=models.ManyToManyField(related_name='recommend_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
