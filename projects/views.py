from django.shortcuts import render
from common.backend import Functions
from .models import Project, Chapter


def index(request):
    context = Functions.build_page_context("projects", request)
    projects = Project.objects.all()[:25]
    context["projects"] = projects
    return render(request, 'projects/project.html', context=context)


def project(request, pk):
    # get objects from database
    project_object = Project.objects.get(pk=pk)
    chapters = Chapter.objects.filter(project__pk=pk).order_by("sort")

    # build page context
    context = Functions.build_page_context("chapter", request)
    context["project"] = project_object
    context["chapters"] = chapters
    if chapters.count == 0:
        empty = Chapter
        empty.title = "Coming Soon"
        context["selected"] = empty
    else:
        context["selected"] = chapters[0]

    return render(request, "projects/chapter.html", context=context)


def chapter(request, project_pk, chapter_sort):
    # get objects from database
    project_object = Project.objects.get(pk=project_pk)
    chapters = Chapter.objects.filter(project__pk=project_pk).order_by("sort")
    selected = filter(lambda c: c.sort == chapter_sort, chapters)

    # build page context
    context = Functions.build_page_context("chapter", request)
    context["project"] = project_object
    context["chapters"] = chapters
    context["selected"] = selected

    return render(request, "projects/chapter.html", context=context)

