# Generated by Django 3.0.4 on 2020-05-19 19:33

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('regno', models.IntegerField(primary_key=True, serialize=False, verbose_name='Register Number')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=6)),
                ('studentcontactno', models.CharField(blank=True, max_length=15, null=True, verbose_name='Students Contact No')),
                ('emailid', models.CharField(blank=True, max_length=80, null=True, verbose_name='Email Id')),
                ('dateofbirth', models.DateField(default='2000-01-01')),
                ('permanentaddress', models.CharField(blank=True, max_length=150, null=True, verbose_name='Permanent Address')),
                ('temporaryaddress', models.CharField(blank=True, max_length=150, null=True, verbose_name='Temporary Address')),
                ('category', models.CharField(default='General', max_length=20)),
                ('specialreservation', models.CharField(blank=True, max_length=30, null=True, verbose_name='Special Reservation')),
                ('religion', models.CharField(blank=True, max_length=15, null=True)),
                ('bloodgroup', models.CharField(blank=True, choices=[('A+ve', 'A+ve'), ('A-ve', 'A-ve'), ('B+ve', 'B+ve'), ('B-ve', 'B-ve'), ('AB+ve', 'AB+ve'), ('AB-ve', 'AB-ve'), ('O+ve', 'O+ve'), ('O-ve', 'O-ve')], max_length=6, null=True, verbose_name='Blood Group')),
                ('personwithdisabilities', models.CharField(blank=True, max_length=40, null=True, verbose_name='Person with Disabilities')),
                ('branch', models.CharField(choices=[('CS', 'Computer Science And Engineering'), ('IT', 'Information Technology'), ('EEE', 'Electrical & Electronics Engineering'), ('EC', 'Electronics & Communication'), ('SFE', 'Safety & Fire Engineering'), ('CE', 'Civil Engineering'), ('ME', 'Mechanical Engineering')], max_length=15)),
                ('cursem', models.CharField(choices=[('1', 'S1'), ('2', 'S2'), ('3', 'S3'), ('4', 'S4'), ('5', 'S5'), ('6', 'S6'), ('7', 'S7'), ('8', 'S8')], max_length=2, verbose_name='Semester')),
                ('section', models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=1)),
                ('photo', models.FileField(blank=True, null=True, upload_to=student.models.student_photo_location)),
                ('status', models.CharField(choices=[('Active', 'Currently Studying'), ('Pass out', 'Course Completed'), ('Drop out', 'Drop out ')], default='Active', max_length=20)),
                ('join', models.IntegerField(choices=[(2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], verbose_name='Year Of Join')),
                ('admissionno', models.IntegerField(default='0', verbose_name='Admission Number')),
                ('admtype', models.CharField(choices=[('Regular', 'Regular'), ('Lateral Entry', 'Lateral Entry')], default='Regular', max_length=20)),
                ('catrank', models.IntegerField(default='0', verbose_name='CAT Rank')),
                ('tenboard', models.CharField(blank=True, max_length=20, null=True, verbose_name='10th Board')),
                ('tenregisterno', models.CharField(blank=True, max_length=20, null=True, verbose_name='10th Register No')),
                ('tenmarks', models.IntegerField(blank=True, null=True, verbose_name='10th Marks')),
                ('tenpercentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='10th Percentage')),
                ('tenyear', models.IntegerField(default='0')),
                ('qualifyingboard', models.CharField(blank=True, max_length=20, null=True, verbose_name='Qualifying Board')),
                ('qualifyingregisterno', models.IntegerField(blank=True, null=True, verbose_name='Qualifying Register No')),
                ('qualifyingmarks', models.IntegerField(blank=True, null=True, verbose_name='Qualifying Marks')),
                ('qualifyingpercentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Qualifying Percentage')),
                ('qualifyingyear', models.IntegerField(blank=True, null=True, verbose_name='Qualifying Year')),
                ('parentorguardianname', models.CharField(blank=True, max_length=50, null=True, verbose_name='Parent/Guardians Name')),
                ('parentorguardianoccupation', models.CharField(blank=True, max_length=25, null=True, verbose_name='Parent/Guardians Occupation')),
                ('parentorguardiancontactno', models.CharField(blank=True, max_length=15, null=True, verbose_name='Parent/Guardians Contact No')),
                ('parentorguardianemailid', models.CharField(blank=True, max_length=50, null=True, verbose_name='Parent/Guardians Email Id')),
                ('miniproject', models.CharField(blank=True, max_length=100, null=True, verbose_name='Mini Project')),
                ('miniprojectguide', models.CharField(blank=True, max_length=25, null=True, verbose_name='Mini Project Guide')),
                ('mainproject', models.CharField(blank=True, max_length=100, null=True, verbose_name='Main Project')),
                ('mainprojectguide', models.CharField(blank=True, max_length=25, null=True, verbose_name='Main Project Guide')),
                ('behaviour', models.CharField(blank=True, default='Good', max_length=100, null=True)),
            ],
            options={
                'ordering': ('regno',),
            },
        ),
    ]
