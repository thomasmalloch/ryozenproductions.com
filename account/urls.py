from django.urls import path, include
from . import views

urlpatterns = [

    path('view', views.account, name='account'),
    path('settings', views.account_settings, name='account_settings'),
    path('security', views.account_security, name='account_security'),
    path('notifications', views.account_notification_settings, name='account_notifications'),
]
