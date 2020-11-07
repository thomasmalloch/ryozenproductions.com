from django.contrib import admin
from .models import Comment, Chapter, Project, Tag


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Project, ProjectAdmin)
admin.site.register(Chapter)
admin.site.register(Comment)
admin.site.register(Tag)
