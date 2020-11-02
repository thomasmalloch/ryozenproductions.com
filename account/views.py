from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from common.backend import Functions, Gravatar


@login_required(redirect_field_name='index')
def account(request):
    context = Functions.build_page_context("my_account", request)
    context["gravatar_large"] = Gravatar.url(request.user.email, size=256)
    return render(request, 'news/account/account.html', context=context)


@login_required(redirect_field_name='index')
def account_settings(request):
    context = Functions.build_page_context("account_settings", request)
    context["gravatar_large"] = Gravatar.url(request.user.email, size=256)
    return render(request, 'news/account/settings.html', context=context)


@login_required(redirect_field_name='index')
def account_security(request):
    context = Functions.build_page_context("account_security", request)
    context["gravatar_large"] = Gravatar.url(request.user.email, size=256)
    return render(request, 'news/account/security.html', context=context)


@login_required(redirect_field_name='index')
def account_notification_settings(request):
    context = Functions.build_page_context("account_notification_settings", request)
    context["gravatar_large"] = Gravatar.url(request.user.email, size=256)
    return render(request, 'news/account/notificationsettings.html', context=context)

