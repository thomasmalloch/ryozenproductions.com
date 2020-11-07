from django.urls import path, include
from . import views

urlpatterns = [
    path('theme/<str:theme>/', views.change_theme, name='change_theme'),
]