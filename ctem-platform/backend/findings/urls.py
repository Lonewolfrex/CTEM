from django.urls import path
from . import views

app_name = "findings"

urlpatterns = [
    path("", views.finding_list, name="list"),
]