from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Finding


def finding_list(request):

    findings = Finding.objects.all().order_by("-created_at")

    return render(
        request,
        "findings/list.html",
        {
            "findings": findings
        }
    )


def finding_detail(request, pk):

    finding = get_object_or_404(
        Finding,
        pk=pk
    )

    return render(
        request,
        "findings/detail.html",
        {
            "finding": finding
        }
    )