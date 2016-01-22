from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    # previous login view
    # url(r'^login/$', views.user_login, name='login'),
    # login / logout urls
    url(r'^login/$',
        'django.contrib.auth.views.login',
        name='login'),
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        {'template_name': 'account/logout.html'},
        name='logout'),
    url(r'^logout-then-login/$',
        'django.contrib.auth.views.logout_then_login',
        name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),

    url(r'^password-change/$',
        'django.contrib.auth.views.password_change',
        {'template_name': 'account/password_change_form.html'},
        name='password_change'),
    url(r'^password-change/done/$',
        'django.contrib.auth.views.password_change_done',
        {'template_name': 'account/password_change_done.html'},
        name='password_change_done'),
]
