from django.db import models
from repositories.models import Repository
from scans.models import ScanJob

class Finding(models.Model):

    SEVERITY=[
        ("CRITICAL","CRITICAL"),
        ("HIGH","HIGH"),
        ("MEDIUM","MEDIUM"),
        ("LOW","LOW"),
        ("INFO","INFO")
    ]

    STATUS=[
        ("OPEN","OPEN"),
        ("IN_PROGRESS","IN_PROGRESS"),
        ("RESOLVED","RESOLVED"),
        ("ACCEPTED","ACCEPTED")
    ]

    repository=models.ForeignKey(Repository,on_delete=models.CASCADE)
    scan=models.ForeignKey(ScanJob,on_delete=models.CASCADE,related_name="findings")

    tool=models.CharField(max_length=100)
    title=models.CharField(max_length=500)
    description=models.TextField()

    severity=models.CharField(max_length=20,choices=SEVERITY)
    status=models.CharField(max_length=20,choices=STATUS,default="OPEN")

    file_path=models.CharField(max_length=500,null=True,blank=True)
    line_number=models.IntegerField(null=True,blank=True)

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title