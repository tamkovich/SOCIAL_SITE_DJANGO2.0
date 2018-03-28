from django.urls import path, re_path
from home.views import HomeView
from home import views

app_name = 'home'

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	re_path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'),
	re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]