from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Repository
from .forms import RepositoryForm
from scans.models import ScanJob
from scans.services.gitleaks_service import (run_gitleaks as execute_gitleaks)
from findings.models import Finding
from scans.services.semgrep_service import (run_semgrep_scan)

def repository_list(request):

    repositories = Repository.objects.select_related(
        "project"
    ).all()

    return render(
        request,
        "repositories/list.html",
        {
            "repositories": repositories
        }
    )

def repository_create(request):

    if request.method == "POST":

        form = RepositoryForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                "repositories:list"
            )

    else:

        form = RepositoryForm()

    return render(
        request,
        "repositories/create.html",
        {
            "form": form
        }
    )

def repository_detail(request, pk):

    repository = get_object_or_404(
        Repository,
        pk=pk
    )
    latest_scan = repository.scans.order_by("-created_at").first()

    return render(
        request,
        "repositories/detail.html",
        {
            "repository": repository,
            "latest_scan": latest_scan
        }
    )

def repository_update(request, pk):

    repository = get_object_or_404(
        Repository,
        pk=pk
    )

    if request.method == "POST":

        form = RepositoryForm(
            request.POST,
            instance=repository
        )

        if form.is_valid():

            form.save()

            return redirect(
                "repositories:list"
            )

    else:

        form = RepositoryForm(
            instance=repository
        )

    return render(
        request,
        "repositories/edit.html",
        {
            "form": form,
            "repository": repository
        }
    )

def repository_delete(request, pk):

    repository = get_object_or_404(
        Repository,
        pk=pk
    )

    if request.method == "POST":

        repository.delete()

        return redirect(
            "repositories:list"
        )

    return render(
        request,
        "repositories/delete.html",
        {
            "repository": repository
        }
    )

def run_gitleaks(request, pk):

    repository = get_object_or_404(
        Repository,
        pk=pk
    )

    scan = ScanJob.objects.create(
        repository=repository,
        tool="GITLEAKS",
        status="RUNNING"
    )

    results = execute_gitleaks(
        repository.git_url
    )

    for result in results:

        Finding.objects.create(
            scan_job=scan,
            title=result.get("Description", "Secret Found"),
            severity="High",
            file_path=result.get("File"),
            line_number=result.get("StartLine"),
            description=result.get("Match")
        )

        finding_count = len(results)

        scan.result_summary = (
            f"Gitleaks completed successfully. "
            f"{finding_count} findings detected."
        )

        scan.status = "COMPLETED"

        scan.save()

    return redirect(
        "repositories:detail",
        pk=repository.id
    )    

def run_semgrep(request, pk):

    repository = get_object_or_404(
        Repository,
        pk=pk
    )

    scan = ScanJob.objects.create(
        repository=repository,
        tool="SEMGREP",
        status="RUNNING"
    )

    try:

        results = run_semgrep_scan(
            repository.git_url
        )

        finding_count = 0

        for item in results.get(
            "results",
            []
        ):

            extra = item.get(
                "extra",
                {}
            )

            severity = (
                extra.get(
                    "severity",
                    "INFO"
                )
                .capitalize()
            )

            Finding.objects.create(
                repository=repository,
                tool="SEMGREP",
                scan_job=scan,
                title=extra.get(
                    "message",
                    "Semgrep Finding"
                ),
                severity=severity,
                file_path=item.get(
                    "path"
                ),
                line_number=item.get(
                    "start",
                    {}
                ).get(
                    "line"
                ),
                description=extra.get(
                    "message"
                )
            )

            finding_count += 1

        scan.status = "COMPLETED"

        scan.result_summary = (
            f"Semgrep completed successfully. "
            f"{finding_count} findings detected."
        )

    except Exception as e:

        scan.status = "FAILED"

        scan.result_summary = str(e)

    scan.save()

    return redirect(
        "repositories:detail",
        pk=repository.id
    )