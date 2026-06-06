from django.db import models
from repositories.models import Repository
from django.utils import timezone


class ScanJob(models.Model):

    STATUS_CHOICES = [
        ("QUEUED", "Queued"),
        ("RUNNING", "Running"),
        ("COMPLETED", "Completed"),
        ("FAILED", "Failed"),
    ]

    TOOL_CHOICES = [
        ("GITLEAKS", "Gitleaks"),
        ("SEMGREP", "Semgrep"),
        ("TRIVY", "Trivy"),
        ("DEPENDENCY_CHECK", "Dependency Check"),
    ]

    repository = models.ForeignKey(
        Repository,
        on_delete=models.CASCADE,
        related_name="scans"
    )

    name = models.CharField(
        max_length=255,
        default="Scan Job"
    )

    tool = models.CharField(
        max_length=50,
        choices=TOOL_CHOICES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="QUEUED"
    )

    created_at = models.DateTimeField(
        default=timezone.now
    )

    started_at = models.DateTimeField(
        null=True,
        blank=True
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    output_file = models.TextField(
        blank=True,
        null=True
    )

    log = models.TextField(
        blank=True,
        null=True
    )

    result_summary = models.TextField(
        blank=True,
        null=True
    )
    
    def __str__(self):
        return f"{self.repository.name} - {self.tool}"