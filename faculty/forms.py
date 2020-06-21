from django import forms
from .models import Faculty


class FacultyModelForm(forms.ModelForm):
    # dob = forms.DateField(input_formats=DATE_INPUT_FORMATS, help_text='dd-mm-yyyy')

    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    datejoin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    dateresig = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    ename = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+'}), label='Name')

    class Meta:
        model = Faculty
        fields = '__all__'
        exclude = ('dateresig', 'dept',)

    def __init__(self, *args, **kwargs):
        super(FacultyModelForm, self).__init__(*args, **kwargs)
        self.fields['ename'].widget.attrs['style'] = 'width:280px;'
        self.fields['desig'].widget.attrs['style'] = 'width:200px;'
        self.fields['ename'].widget.attrs['style'] = 'width:280px;'
        self.fields['permaddr'].widget.attrs['style'] = 'width:400px;height:150px'
        self.fields['tempaddr'].widget.attrs['style'] = 'width:400px;height:150px'
        self.fields['email'].widget.attrs['style'] = 'width:300px;'
        self.fields['permaddr'].label = 'Permenant Address'
        self.fields['tempaddr'].label = 'Temporary Address'
        self.fields['dob'].label = 'Date Of Birth'
        self.fields['datejoin'].label = 'Date Of Join'
        self.fields['dateresig'].label = 'Date Of Resignation'
        self.fields['empid'].label = 'Faculty ID'
        self.fields['contact'].label = 'Contact Number'

        self.fields['dateresig'].required = False
