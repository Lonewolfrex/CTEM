from django.shortcuts import render


def integration_list(request):

    return render(
        request,
        "integrations/list.html"
    )