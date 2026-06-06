from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ScanJob
from .serializers import ScanJobSerializer

from repositories.models import Repository
from django.shortcuts import get_object_or_404

def scan_list(request):

    scans = ScanJob.objects.all().order_by("-created_at")

    return render(
        request,
        "scans/list.html",
        {
            "scans": scans
        }
    )

def scan_detail(request, pk):

    scan = get_object_or_404(
        ScanJob,
        pk=pk
    )

    findings = scan.findings.all()

    return render(
        request,
        "scans/detail.html",
        {
            "scan": scan,
            "findings": findings
        }
    )

class TriggerScanView(APIView):

    def post(self, request):

        repo_id = request.data.get("repository_id")
        tool = request.data.get("tool")

        repo = Repository.objects.get(id=repo_id)

        scan = ScanJob.objects.create(
            name=f"{repo.name}-{tool}-scan",
            repository=repo,
            tool=tool,
            status="QUEUED"
        )

        return Response(
            ScanJobSerializer(scan).data
        )