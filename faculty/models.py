from django.db import models
import datetime

DEPARTMENTS = (('CS', 'Computer Science And Engineering'), ('IT', 'Information Technology'),
               ('EEE', 'Electrical & Electronics Engineering'), ('EC', 'Electronics & Communication'),
               ('SFE', 'Safety & Fire Engineering'), ('CE', 'Civil Engineering'),
               ('ME', 'Mechanical Engineering'))



SEMESTERS = (('1', 'S1'), ('2', 'S2'), ('3', 'S3'), ('4', 'S4'), ('5', 'S5'), ('6', 'S6'), ('7', 'S7'),
             ('8', 'S8'))
   
class Syllabus(models.Model):

    YEARS = []
    limit = datetime.datetime.today().year + 10
    for x in range(2015, limit):
        YEARS.append((x, x))

    year = models.PositiveIntegerField(choices=YEARS)
    dept = models.CharField(max_length=60, choices=DEPARTMENTS, verbose_name="Department")

    theory_max_internal = models.PositiveIntegerField()
    theory_max_external = models.PositiveIntegerField()

    lab_max_internal = models.PositiveIntegerField()
    lab_max_external = models.PositiveIntegerField()


class Subject_Profile(models.Model):

    SUB_TYPES = (("T", "Theory"), ("L", "Practical"), ("P", "Project"))


    syllabussubid = models.ForeignKey(Syllabus, on_delete=models.CASCADE, default="1")
    code = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=70)
    branch = models.CharField(max_length=70, choices=DEPARTMENTS)
    sem = models.CharField(max_length=2, choices=SEMESTERS)
    stype = models.CharField(max_length=15, choices=SUB_TYPES)
    credit = models.IntegerField(default=3)

class Faculty(models.Model):


    DESIG = (
        ("Associate Professor", "Associate Professor"),
        ("Professor", "Professor"),
        ("Guest Faculty", "Guest Faculty"),
        ("Assistant Professor", "Assistant Professor"),
    )

    CATEGORY = (("Permanent", "Permanent"), ("Temporary", "Temporary"))

    
    empid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=30)
    dept = models.CharField(max_length=70, choices=DEPARTMENTS, verbose_name="Department")
    dob = models.DateField(help_text="dd-mm-yyyy")
    desig = models.CharField(
        max_length=20, choices=DESIG, default="Prof", verbose_name="Designation"
    )
    permaddr = models.TextField(max_length=50)
    tempaddr = models.TextField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY, default="Temporary")
    email = models.EmailField()
    contact = models.CharField(max_length=13)
    status = models.CharField(max_length=10)
    datejoin = models.DateField(null=True, blank=True)
    dateresig = models.DateField(null=True, blank=True)


class FacultySubject(models.Model):
 

    YEARS = []
    limit = datetime.datetime.today().year + 10
    for x in range(2015, limit):
        YEARS.append((x, x))

    SECTION = (("A", "A"), ("B", "B"))

    empid = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    subcode = models.OneToOneField(
        Subject_Profile, on_delete=models.CASCADE, verbose_name="Subject Code"
    )
    sem = models.CharField(
        max_length=2, choices=SEMESTERS, default="0", verbose_name="Semester"
    )
    branch = models.CharField(
        max_length=50, choices=DEPARTMENTS, default="A", verbose_name="Branch"
    )
    section = models.CharField(
        max_length=1, choices=SECTION, default="A", verbose_name="Section"
    )
    year = models.IntegerField(choices=YEARS, verbose_name="Year Of Join")
