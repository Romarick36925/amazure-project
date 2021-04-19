from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'Account'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^user_profile/$', views.profile, name='user_profile'),
    path('activate/<slug:uidb64>/<slug:token>/',
         views.activate, name='activate'),
]
