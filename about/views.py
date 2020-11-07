from django.shortcuts import render
from common.backend import Functions


def about(request):
    context = Functions.build_page_context("about", request)
    return render(request, "about/about.html", context=context)

