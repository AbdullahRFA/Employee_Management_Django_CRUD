from django.forms import ModelForm
from .models import Employee
class EmployeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'