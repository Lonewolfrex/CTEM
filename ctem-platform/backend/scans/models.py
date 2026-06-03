from django.db import models
from django.utils import timezone
from repositories.models import Repository


class ScanJob(models.Model):

    STATUS_CHOICES = [
        ("QUEUED", "Queued"),
        ("RUNNING", "Running"),
        ("COMPLETED", "Completed"),
        ("FAILED", "Failed"),
    ]

    name = models.CharField(max_length=255, blank=True, null=True)

    repository = models.ForeignKey(
        Repository,
        on_delete=models.CASCADE,
        related_name="scans"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="QUEUED"
    )

    tool = models.CharField(max_length=100)

    created_at = models.DateTimeField(default=timezone.now)

    started_at = models.DateTimeField(
        null=True,
        blank=True
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    log = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name} - {self.status}"