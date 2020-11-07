from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('project/<slug:slug>/', views.project_view, name='project'),
    path('project/<slug:project_slug>/<int:chapter_sort>/', views.chapter_view, name='chapter'),

    path('project/make-project/', views.edit_project, name='make_project'),
    path('project/<slug:project_slug>/edit/', views.edit_project, name='edit_project'),
    path('project/<slug:project_slug>/action/<str:action>/', views.project_action, name='project_action'),

    path('project/<slug:project_slug>/make-chapter/', views.edit_chapter, name='make_chapter'),
    path('project/<slug:project_slug>/<int:chapter_sort>/edit/', views.edit_chapter, name='edit_chapter'),
    path('project/<slug:project_slug>/<int:chapter_sort>/action/<str:action>/',
         views.chapter_action,
         name='chapter_action'),

]
