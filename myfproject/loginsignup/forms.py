from django import forms
from .models import *


class EmpsignupForm(forms.Form):
    employee_name=forms.CharField(max_length=150)
    employee_ID=forms.CharField(max_length=7)
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=20,widget=forms.PasswordInput)
    contact_number=forms.CharField(max_length=10)
    email=forms.EmailField(max_length=200)


class EmploginForm(forms.Form):
    employee_ID = forms.CharField(max_length=7)
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)

# class AddCompanybranches(forms.Form):
#
#     company_Lname=forms.CharField(max_length=25)
#     Manager_Name=forms.CharField(max_length= 25)
#     branch_ConNo=forms.CharField(max_length=10)
#     branch_address=forms.Textarea()
#
# class AddBranchAccounts(forms.Form):
#     branch_name=forms.CharField(max_length=25)
#     Yearstart=forms.IntegerField()
#     yearsCompleted=forms.CharField(max_length=1)
#     Investment=forms.IntegerField()
#     total_profit=forms.IntegerField()
#
# class AddEmployeDetails(forms.Form):
#     branch_name=forms.CharField(max_length=25)
#     name_emp=forms.CharField(max_length=25)
#     Yearofjoin=forms.IntegerField()
#     Designation=forms.CharField(max_length=5)
#
# class Addproject(forms.Form):
#     branch_name=forms.CharField(max_length=25)
#     totalemp_branch=forms.IntegerField()
#     number_projects=forms.IntegerField()
#     project_name=forms.CharField(max_length=50)
#     manager_name=forms.CharField(max_length=25)
#     emp_inproject=forms.IntegerField()
#     projectincome=forms.IntegerField()
class AddCompanybranches(forms.ModelForm):
    class Meta:
        model= Companybranches
        fields='__all__'

class AddBranchAccounts(forms.ModelForm):
    class Meta:
        model= BranchAccounts
        fields='__all__'

class AddEmployeDetails(forms.ModelForm):
    class Meta:
        model= EmployeDetails
        fields='__all__'

class Addproject(forms.ModelForm):
    class Meta:
        model= project
        fields='__all__'