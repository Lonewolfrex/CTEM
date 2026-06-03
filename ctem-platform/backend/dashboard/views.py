from django.shortcuts import render

from projects.models import Project
from repositories.models import Repository
from assets.models import Asset
from findings.models import Finding
from scans.models import ScanJob

def dashboard(request):

    context = {
        "project_count": Project.objects.count(),
        "repository_count": Repository.objects.count(),
        "asset_count": Asset.objects.count(),
        "finding_count": Finding.objects.count(),
        "scan_count": ScanJob.objects.count(),
    }


    return render(request,"dashboard/dashboard.html",context)