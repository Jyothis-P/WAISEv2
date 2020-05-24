import datetime

from django.db import models
from django.urls import reverse

from faculty.models import Faculty

DEPARTMENTS = (('CS', 'Computer Science And Engineering'), ('IT', 'Information Technology'),
               ('EEE', 'Electrical & Electronics Engineering'), ('EC', 'Electronics & Communication'),
               ('SFE', 'Safety & Fire Engineering'), ('CE', 'Civil Engineering'),
               ('ME', 'Mechanical Engineering'))

SEMESTERS = (('1', 'S1'), ('2', 'S2'), ('3', 'S3'), ('4', 'S4'), ('5', 'S5'), ('6', 'S6'), ('7', 'S7'),
             ('8', 'S8'))

SECTION = (('A', 'A'), ('B', 'B'))

GENDER = (('M', 'Male'), ('F', 'Female'))

SUB_TYPES = (('T', 'Theory'), ('L', 'Practical'), ('P', 'Project'))

EXAMS = (('Internal', 'Internal'), ('External', 'External'))


def student_photo_location(instance, filename):
    extension = filename.split('.')[-1]
    return f'student/reg_photos/{instance.regno}.{extension}'


class Student(models.Model):
    STATUS = (('Active', 'Currently Studying'), ('Pass out', 'Course Completed'),
              ('Drop out', 'Drop out '))

    BLOODGROUPS = (('A+ve', 'A+ve'), ('A-ve', 'A-ve'), ('B+ve', 'B+ve'),
                   ('B-ve', 'B-ve'), ('AB+ve', 'AB+ve'), ('AB-ve', 'AB-ve'),
                   ('O+ve', 'O+ve'), ('O-ve', 'O-ve'),)

    limit = datetime.datetime.today().year + 1
    YEARS = tuple([(x, x) for x in range(2015, 2025)])

    ADMISSION_TYPE = (('Regular', 'Regular'), ('Lateral Entry', 'Lateral Entry'))

    regno = models.IntegerField(primary_key=True, verbose_name='Register Number')

    # Bio Data.
    name = models.CharField(max_length=30, verbose_name='Name')
    gender = models.CharField(max_length=6, choices=GENDER, default='M')
    studentcontactno = models.CharField(max_length=15, verbose_name='Students Contact No', null=True, blank=True)
    emailid = models.CharField(max_length=80, verbose_name=u'Email Id', null=True, blank=True)
    dateofbirth = models.DateField(verbose_name='Date of birth', default='2000-01-01')
    permanentaddress = models.CharField(max_length=150, verbose_name='Permanent Address', null=True, blank=True)
    temporaryaddress = models.CharField(max_length=150, verbose_name='Temporary Address', null=True, blank=True)
    category = models.CharField(max_length=20, default='General')
    specialreservation = models.CharField(max_length=30, verbose_name='Special Reservation', null=True, blank=True)
    religion = models.CharField(max_length=15, null=True, blank=True)
    bloodgroup = models.CharField(max_length=6, verbose_name='Blood Group', choices=BLOODGROUPS, null=True, blank=True)
    personwithdisabilities = models.CharField(max_length=40, verbose_name='Person with Disabilities', null=True,
                                              blank=True)

    # Current student details.
    branch = models.CharField(max_length=15, choices=DEPARTMENTS)
    cursem = models.CharField(max_length=2, choices=SEMESTERS, verbose_name='Semester')
    section = models.CharField(max_length=1, choices=SECTION)
    photo = models.FileField(upload_to=student_photo_location, null=True, blank=True)

    # Admission details.
    status = models.CharField(max_length=20, choices=STATUS, default='Active')
    join = models.IntegerField(choices=YEARS, verbose_name='Year Of Join')
    admissionno = models.IntegerField(verbose_name='Admission Number', default='0')
    admtype = models.CharField(max_length=20, choices=ADMISSION_TYPE, default='Regular')

    # Academic history.
    catrank = models.IntegerField(verbose_name='CAT Rank', default='0')
    tenboard = models.CharField(max_length=20, verbose_name='10th Board', null=True, blank=True)
    tenregisterno = models.CharField(max_length=20, verbose_name='10th Register No', null=True, blank=True)
    tenmarks = models.IntegerField(verbose_name='10th Marks', null=True, blank=True)
    tenpercentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='10th Percentage', null=True,
                                        blank=True)
    tenyear = models.IntegerField(default='0')
    qualifyingboard = models.CharField(max_length=20, verbose_name='Qualifying Board', null=True, blank=True)
    qualifyingregisterno = models.IntegerField(verbose_name='Qualifying Register No', null=True, blank=True)
    qualifyingmarks = models.IntegerField(verbose_name='Qualifying Marks', null=True, blank=True)
    qualifyingpercentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Qualifying Percentage',
                                               null=True, blank=True)
    qualifyingyear = models.IntegerField(verbose_name='Qualifying Year', null=True, blank=True)

    # Guardian details.
    parentorguardianname = models.CharField(max_length=50, verbose_name='Parent/Guardians Name', null=True, blank=True)
    parentorguardianoccupation = models.CharField(max_length=25, verbose_name='Parent/Guardians Occupation', null=True,
                                                  blank=True)
    parentorguardiancontactno = models.CharField(max_length=15, verbose_name='Parent/Guardians Contact No', null=True,
                                                 blank=True)
    parentorguardianemailid = models.CharField(max_length=50, verbose_name='Parent/Guardians Email Id', null=True,
                                               blank=True)

    # Current Academic details.
    miniproject = models.CharField(max_length=100, verbose_name='Mini Project', null=True, blank=True)
    miniprojectguide = models.CharField(max_length=25, verbose_name='Mini Project Guide', null=True, blank=True)
    mainproject = models.CharField(max_length=100, verbose_name='Main Project', null=True, blank=True)
    mainprojectguide = models.CharField(max_length=25, verbose_name='Main Project Guide', null=True, blank=True)
    behaviour = models.CharField(max_length=100, default='Good', null=True, blank=True)

    # Function to redirect to the homepage after adding to db.
    def get_absolute_url(self):
        return reverse('student:index', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.regno) + ': ' + str(self.name)

    class Meta:
        ordering = ('regno',)  # 'ordering' must be a tuple or list (even if you want to order by only one field).


class Syllabus(models.Model):
    YEARS = []
    limit = datetime.datetime.today().year + 10
    for x in range(2010, limit):
        YEARS.append((x, x))

    year = models.PositiveIntegerField(choices=YEARS)
    dept = models.CharField(max_length=60, choices=DEPARTMENTS, verbose_name='Department')

    def __str__(self):
        return str(self.year)

    class Meta:
        ordering = ('year',)


class Subject(models.Model):
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE, default='1')
    code = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=70)
    branch = models.CharField(max_length=70, choices=DEPARTMENTS)
    sem = models.CharField(max_length=2, choices=SEMESTERS)
    type = models.CharField(max_length=15, choices=SUB_TYPES)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ('code',)


class MarkList(models.Model):
    CHANCES = (('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'))

    YEARS = []
    limit = datetime.datetime.today().year + 10
    for x in range(2015, limit):
        YEARS.append((x, x))

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    branch = models.CharField(max_length=70, choices=DEPARTMENTS)
    sem = models.CharField(max_length=2, choices=SEMESTERS)
    section = models.CharField(max_length=1, choices=SECTION)
    type = models.CharField(max_length=9, choices=EXAMS, default='Internal')
    batch_join_year = models.IntegerField(choices=YEARS, default='0')
    chance = models.IntegerField(default='0', choices=CHANCES)

    def __str__(self):
        return str(self.student) + ' S' + str(self.sem)

    class Meta:
        ordering = ('student',)


class SubjectMarks(models.Model):
    mark_list = models.ForeignKey(MarkList, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.SmallIntegerField(default='0')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.marks)

    class Meta:
        ordering = ('mark_list',)
