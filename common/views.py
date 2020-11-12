from django.shortcuts import redirect
from .backend import Functions
import traceback


def change_theme(request, theme):
    Functions.set_theme(request, theme)
    return redirect('index')


def its500time(request):
    return traceback.format_exc()
