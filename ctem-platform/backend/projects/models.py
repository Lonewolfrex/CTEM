from django.db import models


class Project(models.Model):

    CRITICALITY_CHOICES = [
        ("LOW", "Low"),
        ("MEDIUM", "Medium"),
        ("HIGH", "High"),
        ("CRITICAL", "Critical"),
    ]

    name = models.CharField(
        max_length=255,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    owner = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    criticality = models.CharField(
        max_length=20,
        choices=CRITICALITY_CHOICES,
        default="MEDIUM"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name