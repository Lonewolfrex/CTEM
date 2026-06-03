from django.shortcuts import render
from .models import Finding


def finding_list(request):

    findings = Finding.objects.all()

    return render(
        request,
        "findings/list.html",
        {
            "findings": findings
        }
    )