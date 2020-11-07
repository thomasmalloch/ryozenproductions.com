from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.utils.text import slugify
from common.backend import Functions
from .models import Project, Chapter
from .forms import ProjectForm, ChapterForm


def index(request):
    context = Functions.build_page_context("projects", request)
    projects = Project.objects.all()[:25]
    context["projects"] = projects
    return render(request, 'projects/project.html', context=context)


def project_view(request, slug):
    # get objects from database
    project = Project.objects.get(slug=slug)
    chapters = Chapter.objects.filter(project__pk=project.pk).order_by("sort")

    # build page context
    context = Functions.build_page_context("projects", request)
    context["project"] = project
    context["chapters"] = chapters
    if len(chapters) == 0:
        empty = Chapter
        empty.title = "Coming Soon"
        context["selected"] = empty
    else:
        context["selected"] = chapters[0]

    return render(request, "projects/chapter.html", context=context)


def chapter_view(request, project_slug, chapter_sort):
    # get objects from database
    project = Project.objects.get(slug=project_slug)
    chapters = Chapter.objects.filter(project__pk=project.pk).order_by("sort")
    selected = filter(lambda c: c.sort == chapter_sort, chapters)

    # build page context
    context = Functions.build_page_context("projects", request)
    context["project"] = project
    context["chapters"] = chapters
    context["selected"] = selected
    return render(request, "projects/chapter.html", context=context)


@login_required
@permission_required("projects.add_project", raise_exception=True)
@permission_required("projects.change_project", raise_exception=True)
def edit_project(request, project_slug=None):
    if project_slug is None:
        project = Project()
        project.user = request.user
    else:
        project = Project.objects.get(slug=project_slug)

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project.title = form.cleaned_data["title"]
            project.slug = slugify(project.title)
            project.description = form.cleaned_data["description"]
            project.is_public = form.cleaned_data["is_public"]
            project.save()

            return redirect('index')
    else:
        form = ProjectForm(instance=project)

    context = Functions.build_page_context("projects", request)
    context["project"] = project
    context["project_form"] = form
    return render(request, "projects/edit_project.html", context=context)


@login_required
@permission_required("projects.add_chapter", raise_exception=True)
@permission_required("projects.change_chapter", raise_exception=True)
def edit_chapter(request, project_slug, chapter_sort=None):
    project = Project.objects.get(slug=project_slug)
    chapters = Chapter.objects.filter(project__pk=project.pk).order_by("sort")
    if chapter_sort is None:
        chapter = Chapter()
        chapter.user = request.user
        chapter.project = project
        if len(chapters) == 0:
            chapter.sort = 0
        else:
            chapter.sort = int(chapters[-1].sort) + 1
    else:
        chapter = filter(lambda c: c.sort == chapter_sort, chapters)

    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            chapter.title = form.cleaned_data["title"]
            chapter.description = form.cleaned_data["description"]
            chapter.body = form.cleaned_data["body"]
            chapter.is_public = form.cleaned_data["is_public"]
            chapter.save()

            return redirect('chapter', project_slug=project.slug, chapter_sort=chapter.sort)
    else:
        form = ChapterForm(instance=chapter)

    context = Functions.build_page_context("projects", request)
    context["project"] = project
    context["chapters"] = chapters
    context["chapter"] = chapter
    context["chapter_form"] = form
    return render(request, "projects/edit_chapter.html", context=context)


@login_required
@permission_required("projects.change_project", raise_exception=True)
def project_action(request, project_slug, action):
    project = Project.objects.get(slug=project_slug)
    if action == "toggle-public":
        project.is_public = not project.is_public
        project.save()
    elif action == "delete":
        project.delete()

    return redirect('index')


@login_required
@permission_required("projects.change_chapter", raise_exception=True)
def chapter_action(request, project_slug, chapter_sort, action):
    chapter = Chapter.objects.get(project__slug=project_slug, chapter_sort=chapter_sort)
    if action == "toggle-public":
        chapter.is_public = not chapter.is_public
        chapter.save()
    elif action == "delete":
        chapter.delete()
        previous_chapter = chapter_sort - 1
        if previous_chapter < 0:
            previous_chapter = 0

        try:
            return redirect('chapter', project_slug=project_slug, chapter_sort=previous_chapter)
        except:
            return redirect('project', project_slug=project_slug)

    return redirect('chapter', project_slug=project_slug, chapter_sort=chapter_sort)
