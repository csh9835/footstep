from django.db import models
from django.contrib.auth.models import User

class SidebarContent(models.Model):
    category_sub = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_sub

class Post(models.Model):
    subject = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150, null=True, blank=True)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_post')
    category = models.ForeignKey(SidebarContent, on_delete=models.CASCADE)
    recommend = models.ManyToManyField(User, related_name='recommend_post')

    def __str__(self):
        return self.subject

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    recommend = models.ManyToManyField(User, related_name='recommend_comment')