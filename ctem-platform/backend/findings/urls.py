from django.urls import path
from . import views

app_name = "findings"

urlpatterns = [
    path("", views.finding_list, name="list"),
    path("<int:pk>/",views.finding_detail,name="detail"),
]