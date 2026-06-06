from django.urls import path
from . import views

app_name = "repositories"

urlpatterns = [
    path(
        "",
        views.repository_list,
        name="list"
    ),

    path(
        "create/",
        views.repository_create,
        name="create"
    ),

    path(
        "<int:pk>/",
        views.repository_detail,
        name="detail"
    ),
    
    path(
    "<int:pk>/edit/",
    views.repository_update,
    name="edit"
    ),

    path(
        "<int:pk>/delete/",
        views.repository_delete,
        name="delete"
    ),

    path(
        "<int:pk>/run-gitleaks/",
        views.run_gitleaks,
        name="run_gitleaks"
    ),
    
    path(
        "<int:pk>/run-semgrep/",
        views.run_semgrep,
        name="run_semgrep"
    ),   
]