from django.db import models
from django.contrib.auth.models import User

class SidebarContent(models.Model):
    category_sub = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_sub

class Post(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(SidebarContent, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject


#class Comment(models.Model):
    #post = models.ForeignKey(Post, on_delete=models.CASCADE)