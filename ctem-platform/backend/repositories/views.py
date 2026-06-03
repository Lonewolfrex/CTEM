from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Repository
from .forms import RepositoryForm


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

    return render(
        request,
        "repositories/detail.html",
        {
            "repository": repository
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