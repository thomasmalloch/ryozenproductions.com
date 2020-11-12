from django.urls import path, include
from . import views

handler500 = "common.views.its500time"

urlpatterns = [
    path('theme/<str:theme>/', views.change_theme, name='change_theme'),
]
