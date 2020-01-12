from django.db import models
# Create your models here.
class Companybranches(models.Model):

    company_Lname=models.CharField(max_length=25)
    Manager_Name=models.CharField(max_length= 25)
    branch_ConNo=models.CharField(max_length=10)
    branch_address=models.TextField()
    def __str__(self):
        return "{0}".format(self.company_Lname)

class BranchAccounts(models.Model):
    branch_name=models.CharField(max_length=25)
    year_choices= (('1','1 year'),('2','2 years'),('3', '3 years'))
    Yearstart=models.IntegerField()
    yearsCompleted=models.CharField(max_length=1,choices=year_choices)
    Investment=models.IntegerField()
    total_profit=models.IntegerField()
    def __str__(self):
        return '{0}'.format(self.branch_name)


class EmployeDetails(models.Model):
    Des_choice=(('m','manager'),('P','Programer analyst'),('A','Assosiate'))
    branch_name=models.CharField(max_length=25)
    name_emp=models.CharField(max_length=25)
    Yearofjoin=models.IntegerField()
    Designation=models.CharField(max_length=1,choices=Des_choice)
    def __str__(self):
        return '{0}'.format(self.name_emp)
class project(models.Model):
    branch_name=models.CharField(max_length=25)
    totalemp_branch=models.IntegerField()
    number_projects=models.IntegerField()
    project_name=models.CharField(max_length=50)
    manager_name=models.CharField(max_length=25)
    emp_inproject=models.IntegerField()
    projectincome=models.IntegerField()
    def __str__(self):
        return '{0}'.format(self.project_name)






