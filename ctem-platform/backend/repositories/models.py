from django.db import models
from projects.models import Project

class Repository(models.Model):
    name = models.CharField(max_length=255)
    git_url = models.URLField(blank=True, null=True)
    branch = models.CharField(max_length=100, default="main")

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="repositories")

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name