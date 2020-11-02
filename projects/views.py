from django.shortcuts import render
from common.backend import Functions


def index(request):
    context = Functions.build_page_context("news", request)
    posts = [] # Post.objects.order_by("created")[:25]
    context["posts"] = posts
    return render(request, 'projects/project.html', context=context)
