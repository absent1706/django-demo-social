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

    # restore password urls
    url(r'^password-reset/$',
        'django.contrib.auth.views.password_reset',
        {'template_name': 'account/password_reset_form.html',
        'email_template_name':'account/password_reset_email.html'},
        name='password_reset'),
    url(r'^password-reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        {'template_name': 'account/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'account/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^password-reset/complete/$',
        'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'account/password_reset_complete.html'},
        name='password_reset_complete'),

    url(r'^register/$', views.register, name='register'),
]
