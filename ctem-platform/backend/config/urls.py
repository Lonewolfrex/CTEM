from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("dashboard.urls")),

    path("projects/", include("projects.urls")),
    path("repositories/", include("repositories.urls")),
    path("assets/", include("assets.urls")),
    path("scans/", include("scans.urls")),
    path("findings/", include("findings.urls")),
    path("reports/", include("reports.urls")),
    path("integrations/", include("integrations.urls")),
]