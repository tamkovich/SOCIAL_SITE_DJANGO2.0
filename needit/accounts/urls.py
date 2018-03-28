from django.urls import path, re_path
from . import views
from django.contrib.auth.views import (
	login, logout, password_reset, password_reset_done, password_reset_confirm,
	password_reset_complete
)

app_name = 'accounts'

urlpatterns = [
	path('register/', views.register, name='register'),
	path('login/', login, {'template_name': 'accounts/login.html'}, name='login'),
  path('logout/', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
  path('profile/', views.view_profile, name='view_profile'),
  re_path(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
  path('profile/edit/', views.edit_profile, name='edit_profile'),
  path('change-password/', views.change_password, name='change_password'),
  path('reset-password/', password_reset, {'template_name': 'accounts/reset_password.html', 'post_reset_redirect': 'accounts:password_reset_done', 'email_template_name': 'accounts/reset_password_email.html'}, name='reset_password'),
  path('reset-password/done/', password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),
  re_path(r'reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),
  path('reset-password/complete/', password_reset_complete, {'template_name': 'accounts/reset_password_complete.html',}, name='password_reset_complete')
]