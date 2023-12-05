from django  import forms 
from .models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # error_messages = {
        #     'name' : {'required' : 'Your name is required'}
        # }
