from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('project/<int:pk>/', views.project, name='project'),
    #path('project/edit/<int:pk>/', views.edit_project, name='edit_project'),
    #path('project/create/', views.create_project, name='create_project'),

    path('project/<int:project_pk>/<int:chapter_sort>', views.chapter, name='chapter'),
    #path('project/edit/<int:project_pk>/<int:chapter_pk>', views.edit_chapter, name='edit_chapter'),
    #path('project/create/<int:project_pk>/', views.create_chapter, name='create_chapter'),
]
