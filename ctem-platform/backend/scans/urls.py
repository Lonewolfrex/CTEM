from django.urls import path
from . import views

app_name = "scans"

urlpatterns = [
    path("", views.scan_list, name="list"),
    path("run/", views.TriggerScanView.as_view(), name="run"),
]