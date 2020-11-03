from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=100, default="New Project", verbose_name="Title:")
    description = models.CharField(max_length=100, default="Project Description", verbose_name="Description:")
    is_public = models.BooleanField(default=False, verbose_name="Is Public:")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    title = models.CharField(max_length=100, default="New Chapter", verbose_name="Title:")
    description = models.CharField(max_length=100, default="Chapter Description", verbose_name="Description:")
    body = models.TextField(blank=True, null=True, verbose_name="Body:")
    is_public = models.BooleanField(default=False, verbose_name="Is Public:")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    sort = models.IntegerField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return "A comment made on {0}".format(self.date)

    class Meta:
        permissions = [
            ("can_comment", "User can comment on a chapter"),
            ("can_edit_self", "User can edit their own comments"),
            ("can_edit_other", "User can edit other another user's comment"),
            ("can_delete_self", "User can delete their comment"),
            ("can_delete_other", "User can delete another user's comment"),
        ]
