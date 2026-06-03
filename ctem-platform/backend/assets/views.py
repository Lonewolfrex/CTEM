from django.shortcuts import render
from .models import Asset


def asset_list(request):

    assets = Asset.objects.all()

    return render(
        request,
        "assets/list.html",
        {
            "assets": assets
        }
    )