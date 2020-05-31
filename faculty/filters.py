import django_filters

from faculty.models import Faculty


class FacultyFilter(django_filters.FilterSet):
    class Meta:
        model = Faculty
        fields = ["ename", "desig", "category"]
