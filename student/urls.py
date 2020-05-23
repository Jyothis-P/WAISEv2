from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.student_create, name='new'),
    path('csv', views.student_create_csv, name='csv'),
    path('search', views.student_search, name='search'),
    path('detail', views.student_search, name='detail'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.StudentDelete.as_view(), name='delete'),
]
