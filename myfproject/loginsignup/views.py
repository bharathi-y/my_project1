from django.shortcuts import render,HttpResponse,redirect
from .forms import EmploginForm, EmpsignupForm, AddCompanybranches, AddBranchAccounts,AddEmployeDetails,Addproject
from .models import *
#AddBranchAccounts,AddEmployeDetails,Addproject
# Create your views here.
def home_page(request):
    return render(request,'home_page.html',context={})
def login_page(request):
    return render(request ,'login_page.html',context={})
def signup_page(request):
    return render(request,'signup_page.html',context={})
def emplogin_page(request):
    elogin_form=EmploginForm()
    return render (request,'emplogin_page.html',context={'elform':elogin_form})
def empsignup_page(request):
    esignin_form=EmpsignupForm()
    return render(request,'empsignup_page.html',context={'esform': esignin_form})
#all tabeles retrive
def allCB_page(request):
    allCB=Companybranches.objects.all
    return render(request,'Companybranches.html',context={'allCB':allCB})
def allBA_page(request):
    allBA=BranchAccounts.objects.all
    return render(request,'BranchAccounts.html',context={'allBA':allBA})
def allED_page(request):
    allED=EmployeDetails.objects.all
    return render (request,'EmployeDetails.html',context={'allED':allED})
def allP_page(request):
    allP=project.objects.all
    return render(request,'projects.html',context={'allP':allP})
#----------------------------------------------------------------------------------------------------------
# Companybranche add items
def addCB_page(request):
    if request.method =='POST':
        addCB=AddCompanybranches(request.POST)
        if addCB.is_valid():
            addCB.save()
            return redirect('Companybranches_page')
    else :
        addCB=AddCompanybranches()
    return render(request,'AddCompanybranches.html',context={'addCB':addCB})
#edit Companybranche
def edCB_page(request,pk=None):
    obj = Companybranches.objects.get(id=pk)
    if request.method == 'POST':
        edCB = AddCompanybranches(request.POST,instance=obj)
        if edCB.is_valid():
            edCB.save()
            return redirect('Companybranches_page')
    else :
        edCB=AddCompanybranches(instance=obj)
    return render(request,'edCompanybranches.html',context={'edCB':edCB})
#Delete Companybranche
def dlCB_page(request,pk=None):
    obj = Companybranches.objects.get(id=pk)
    obj.delete()
    return redirect('Companybranches_page')

#-----------------------------------------------------------------------------------------------------------------------
#BranchAccounts add Key

def addBA_page(request):
    if request.method== 'POST' :
        addBA=AddBranchAccounts(request.POST)
        if addBA.is_valid():
            addBA.save()
            return redirect('BranchAccounts_page')
    else:
        addBA=AddBranchAccounts()
    return render(request,'AddBranchAccounts.html',context={'addBA':addBA})
#BranchAccounts edit key

def edBA_page(request,pk=None):
    obj = BranchAccounts.objects.get(id=pk)
    if request.method == 'POST':
        edBA = AddBranchAccounts(request.POST,instance=obj)
        if edBA.is_valid():
            edBA.save()
            return redirect('BranchAccounts_page')
    else :
        edBA=AddBranchAccounts(instance=obj)
    return render(request,'edBranchAccounts.html',context={'edBA':edBA})
#Delete BranchAccounts
def dlBA_page(request,pk=None):
    obj = BranchAccounts.objects.get(id=pk)
    obj.delete()
    return redirect('BranchAccounts_page')

#----------------------------------------------------------------------------------------------------------------------
# Add EmployeDetails Key

def addED_page(request):
    if request.method=='POST':
        addED=AddEmployeDetails(request.POST)
        if addED.is_valid():
            addED.save()
            return redirect('EmployeDetails')
    else:
        addED=AddEmployeDetails()
        return render(request,'AddEmployeDetails.html',context={'addED':addED})
# Edit EmployeDetails key

def edED_page(request, pk=None):
    obj = EmployeDetails.objects.get(id=pk)
    if request.method == 'POST':
        edED = AddEmployeDetails(request.POST, instance=obj)
        if edED.is_valid():
            edED.save()
            return redirect('EmployeDetails')
    else:
        edED = AddCompanybranches(instance=obj)
        return render(request, 'edEmployeDetails.html', context={'edED': edED})

# Delete EmployeDetails key

def dlED_page(request, pk=None):
        obj = EmployeDetails.objects.get(id=pk)
        obj.delete()
        return redirect('EmployeDetails')
#------------------------------------------------------------------------------------
# project Add Key
def addP_page(request):
    if request.method=='POST':
        addP=Addproject(request.POST)
        if addP.is_valid():
            addP.save()
            return redirect('project')
    else:
        addP=Addproject()

    return render(request,'Addprojects.html',context={'addP':addP})

# project edit key
def edP_page(request, pk=None):
    obj = project.objects.get(id=pk)
    if request.method == 'POST':
        edP = Addproject(request.POST, instance=obj)
        if edP.is_valid():
            edP.save()
            return redirect('project')
    else:
        edP = Addproject(instance=obj)
        return render(request, 'edprojects.html', context={'edP': edP})

# Delete Project key

def dlP_page(request, pk=None):
    obj = project.objects.get(id=pk)
    obj.delete()
    return redirect('project')








