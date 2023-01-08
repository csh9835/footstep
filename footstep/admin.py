from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import SidebarContent, Post, Comment
from common.models import Profile

class SomeModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(SidebarContent)
admin.site.register(Post, SomeModelAdmin)
admin.site.register(Profile)
admin.site.register(Comment)