from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FacultyModelForm


def index(request):
    return HttpResponse("Hello, world. You're at the faculty home.")



def faculty_create(request):
    faculty = FacultyModelForm(request.POST or None)

    if faculty.is_valid():
        faculty.save()
        

    context = {
        "form": faculty,
        "title": 'Add Faculty',
    }

    return render(request, 'faculty/faculty_form.html', context)


