from django.contrib import admin
from .models import SidebarContent,Post
from common.models import Profile

admin.site.register(SidebarContent)
admin.site.register(Post)
admin.site.register(Profile)