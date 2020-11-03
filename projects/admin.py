from django.contrib import admin
from .models import Comment, Chapter, Project

admin.site.register(Project)
admin.site.register(Chapter)
admin.site.register(Comment)
