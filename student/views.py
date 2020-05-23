import csv

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView

from student.filters import StudentFilter
from student.forms import StudentModelForm, StudentCsvForm, StudentUpdateForm
from student.models import Student


# TODO: Add user's dept to the queries

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def student_create(request):
    student = StudentModelForm(request.POST or None)

    if student.is_valid():
        instance = student.save(commit=False)
        instance.branch = 'CS'
        # instance.branch = request.user.dept
        instance.save()

        return redirect('student:search')

    context = {
        "form": student,
        "title": 'Add Student',
    }

    return render(request, 'student/student_form.html', context)


def student_create_csv(request):
    if "GET" == request.method:
        data = {
            'title': 'Student CSV'
        }
        return render(request, "student/student_csv.html", data)

    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            return HttpResponseRedirect(reverse("student:csv"))
            # if file is too large, return
        if csv_file.multiple_chunks():
            return HttpResponseRedirect(reverse("student:csv"))

        data = csv.DictReader(csv_file.read().decode('utf-8').splitlines())

        for data_dict in data:

            try:
                form = StudentCsvForm(data_dict)
                # print("-----------", data_dict)
                if form.is_valid():
                    form.save()
                else:
                    lst = []
                    for i in form.errors:
                        lst.append(str((i, form.errors[i])) + ' | ' + str(data_dict['name']))

                    print(lst)
                    # return render(request, "student/faculty_attendance_main.html", {'obj': lst})
            except Exception as e:
                print(repr(e))
                pass

    except Exception as e:
        print(repr(e))

    return HttpResponseRedirect(reverse("student:index"))


def student_search(request):
    if request.method == 'GET':
        student_list = Student.objects.all().order_by('regno')
        student_filter = StudentFilter(request.GET, queryset=student_list)
        return render(request, 'student/student_list.html', {'filter': student_filter, 'title': 'Student Search'})


def student_update(request, pk):
    instance = get_object_or_404(Student, regno=pk)
    student = StudentUpdateForm(request.POST or None, request.FILES or None, instance=instance)
    if student.is_valid():
        instance = student.save(commit=False)
        instance.save()

        return redirect('student:search')
    context = {
        "form": student,
        "title": 'Edit Student',
    }

    return render(request, 'student/student_form.html', context)


class StudentDelete(DeleteView):
    model = Student

    def get_success_url(self):
        url = self.request.GET['next']
        params = url.split('?')[1]
        base = reverse('student:search')
        url = f'{base}?{params}'
        return url
