from django.shortcuts import render


def report_list(request):

    return render(
        request,
        "reports/list.html"
    )