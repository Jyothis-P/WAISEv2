import datetime

from django import forms
from .models import Student


class StudentModelForm(forms.ModelForm):
    end_limit = datetime.datetime.today().year + 1
    start_limit = datetime.datetime.today().year - 6
    YEAR_RANGE = tuple([(x, x) for x in range(start_limit, end_limit)])

    name = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+'}), label='Student Name')
    dateofbirth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    qualifyingyear = forms.CharField(widget=forms.Select(choices=YEAR_RANGE), label='Qualifying Year')
    tenyear = forms.CharField(widget=forms.Select(choices=YEAR_RANGE), label='10th Qualifying Year')
    permanentaddress = forms.CharField(widget=forms.Textarea())
    temporaryaddress = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['branch']

    def __init__(self, *args, **kwargs):
        super(StudentModelForm, self).__init__(*args, **kwargs)
        self.fields['permanentaddress'].widget.attrs['style'] = 'width:400px;height:180px;margin-bottom:10px;'
        self.fields['temporaryaddress'].widget.attrs['style'] = 'width:400px;height:180px;margin-bottom:10px;'
        self.fields['status'].widget.attrs['style'] = 'width:200px;'
        self.fields['religion'].widget.attrs['style'] = 'width:200px;'
        self.fields['studentcontactno'].widget.attrs['style'] = 'width:150px;'

        self.fields['tenyear'].label = '10th Year of Passout'
        self.fields['cursem'].label = 'Semester'
        self.fields['join'].label = 'Year of Join'
        self.fields['admtype'].label = 'Admission Type'
        self.fields['permanentaddress'].label = 'Permanent Address'
        self.fields['temporaryaddress'].label = 'Temporary Address'
        self.fields['dateofbirth'].label = 'Date of Birth'


class StudentCsvForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ('photo',)


class StudentUpdateForm(forms.ModelForm):
    regno = forms.IntegerField(disabled=True, widget=forms.TextInput(attrs={'size': 2}))
    permanentaddress = forms.CharField(widget=forms.Textarea())
    temporaryaddress = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)
        self.fields['permanentaddress'].widget.attrs['style'] = 'width:400px;height:180px'
        self.fields['temporaryaddress'].widget.attrs['style'] = 'width:400px;height:180px'
        self.fields['status'].widget.attrs['style'] = 'width:180px;'
        self.fields['branch'].widget.attrs['style'] = 'width:320px;'
        self.fields['regno'].label = 'Register Number'
        self.fields['name'].label = 'Student Name'
        self.fields['cursem'].label = 'Semester'
        self.fields['join'].label = 'Year of Join'
        self.fields['admtype'].label = 'Admission Type'
