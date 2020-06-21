from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import FacultyModelForm


def index(request):
    return HttpResponse("Hello, world. You're at the faculty home.")



def faculty_create(request):
    student = FacultyModelForm(request.POST or None)

    context = {
        "form": student,
        "title": 'Add Student',
    }

    return render(request, 'faculty/faculty_form.html', context)


