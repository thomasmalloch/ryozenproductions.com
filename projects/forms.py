from django import forms
from .models import Chapter, Project
from django.contrib.auth.models import User


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ("title", "description", "is_public")


class ChapterForm(forms.ModelForm):

    class Meta:
        model = Chapter
        fields = ("title", "description", "body", "is_public")

