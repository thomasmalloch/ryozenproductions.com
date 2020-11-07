from django.shortcuts import redirect
from .backend import Functions


def change_theme(request, theme):
    Functions.set_theme(request, theme)
    return redirect('index')
