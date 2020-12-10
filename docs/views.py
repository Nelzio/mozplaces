from django.shortcuts import render


def documentation_views(request):
    return render(request, "docs/index.html")
