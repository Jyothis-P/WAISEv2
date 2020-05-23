import django_filters

from student.models import Student


class StudentFilter(django_filters.FilterSet):
    dateofbirth = django_filters.DateFilter(input_formats=['%d-%m-%Y'])

    class Meta:
        model = Student
        fields = ['cursem', 'join', 'regno', 'dateofbirth', 'branch', 'status']
