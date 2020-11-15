import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")


class Project(models.Model):
    title = models.CharField(max_length=100, default="New Project", verbose_name="Title:")
    description = models.TextField(blank=True, default="Project Description", verbose_name="Description:")
    is_public = models.BooleanField(default=False, verbose_name="Is Public:")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, default=slugify(uuid.uuid4()))
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.title) + " • " + str(self.description)


class Chapter(models.Model):
    title = models.CharField(max_length=100, default="New Chapter", verbose_name="Title:")
    description = models.CharField(max_length=100, default="Chapter Description", verbose_name="Description:")
    body = models.TextField(blank=True, null=True, verbose_name="Body:")
    is_public = models.BooleanField(default=False, verbose_name="Is Public:")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    sort = models.IntegerField()

    def __str__(self):
        return str(self.sort) + " • " + str(self.title) + " Project: " + str(self.project.title)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return "A comment made on {0}".format(self.date)

    class Meta:
        permissions = [
            ("change_other", "User can edit other another user's comment"),
            ("delete_other", "User can delete another user's comment"),
        ]
