from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^new/$', views.student_create, name='new'),
    url(r'^csv/$', views.student_create_csv, name='csv'),
    url(r'^search/$', views.student_search, name='search'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.student_update, name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.StudentDelete.as_view(), name='delete'),
]
