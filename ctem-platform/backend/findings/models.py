from django.db import models
from scans.models import ScanJob
from repositories.models import Repository

class Finding(models.Model):

    SEVERITY_CHOICES = [
        ("Critical", "Critical"),
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
        ("Info", "Info"),
    ]

    STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("FIXED", "Fixed"),
        ("ACCEPTED", "Accepted"),
    ]

    repository = models.ForeignKey(
        Repository,
        on_delete=models.CASCADE,
        related_name="findings",
        null=True,
        blank=True
    )

    tool = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    scan_job = models.ForeignKey(
        ScanJob,
        on_delete=models.CASCADE,
        related_name="findings",
        null=True,
        blank=True
    )

    title = models.CharField(
        max_length=500
    )

    severity = models.CharField(
        max_length=20,
        choices=SEVERITY_CHOICES,
        default="Low"
    )

    file_path = models.TextField(
        blank=True,
        null=True
    )

    line_number = models.IntegerField(
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="OPEN"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title