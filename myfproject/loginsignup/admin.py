from django.contrib import admin
from .models import Companybranches,BranchAccounts,EmployeDetails,project

@admin.register(Companybranches)
class CompanybranchesAdmin(admin.ModelAdmin):
    list_display=["company_Lname","Manager_Name","branch_ConNo","branch_address"]

@admin.register(BranchAccounts)
class BranchAccountsAdmin(admin.ModelAdmin):
    list_display = ["branch_name", "Yearstart", "yearsCompleted", "Investment", "total_profit"]

@admin.register(EmployeDetails)
class EmployeDetailsAdmin(admin.ModelAdmin):
    list_display = ["branch_name","name_emp","Yearofjoin","Designation"]

@admin.register(project)
class projectAdmin(admin.ModelAdmin):
    list_display = ["branch_name","totalemp_branch","number_projects","project_name","manager_name","emp_inproject","projectincome"]

# Register your models here.
