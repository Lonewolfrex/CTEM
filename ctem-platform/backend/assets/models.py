from django.db import models
from projects.models import Project

class Asset(models.Model):

    TYPE=[
        ("API","API"),
        ("DOMAIN","DOMAIN"),
        ("SERVER","SERVER"),
        ("CONTAINER","CONTAINER"),
        ("REPOSITORY","REPOSITORY")
    ]

    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name="assets")

    asset_type=models.CharField(max_length=50,choices=TYPE)
    name=models.CharField(max_length=255)
    identifier=models.CharField(max_length=255)

    criticality=models.CharField(max_length=20,default="MEDIUM")

    def __str__(self):
        return self.name