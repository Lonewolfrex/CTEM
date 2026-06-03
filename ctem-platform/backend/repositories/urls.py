from django.urls import path
from . import views

app_name = "repositories"

urlpatterns = [
    path("", views.repository_list, name="list"),
    path("api/", views.RepositoryApiView.as_view(), name="api"),
]