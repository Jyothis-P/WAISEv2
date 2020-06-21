from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="faculty-index"),
    path("new/", views.faculty_create, name="faculty-new"),
]
