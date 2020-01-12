"""myfproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from loginsignup import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page,name='home_page'),
    path('login_page/',views.login_page,name='login_page'),
    path('signup_page/',views.signup_page,name='signup_page'),
    path('emplogin_page/',views.emplogin_page,name='emplogin_page'),
    path('empsignup_page/',views.empsignup_page,name='empsignup_page'),

    path('Companybranches/',views.allCB_page,name ='Companybranches_page'),
    path('BranchAccounts/',views.allBA_page,name='BranchAccounts_page'),
    path('EmployeDetails/',views.allED_page,name='EmployeDetails'),
    path('projects/',views.allP_page,name='project'),
#add key
    path('addCompanybranches/',views.addCB_page,name ='addCompanybranches'),
    path('addBranchAccounts/',views.addBA_page,name='addBranchAccounts'),
    path('addEmployeDetails/',views.addED_page,name='addEmployeDetails'),
    path('addprojects/',views.addP_page,name='addproject'),
#edit key
    path('editCompanybranches/<int:pk>/edit',views.edCB_page,name ='edCompanybranches'),
    path('editBranchAccounts/<int:pk>/edit',views.edBA_page,name='edBranchAccounts'),
    path('editEmployeDetails/<int:pk>/edit',views.edED_page,name='edEmployeDetails'),
    path('editprojects/<int:pk>/edit',views.edP_page,name='edproject'),

    #delete key
    path('deleteCompanybranches/<int:pk>/',views.dlCB_page,name ='dlCompanybranches'),
    path('deleteBranchAccounts/<int:pk>/',views.dlBA_page,name='dlBranchAccounts'),
    path('deleteEmployeDetails/<int:pk>/',views.dlED_page,name='dlEmployeDetails'),
    path('deleteprojects/<int:pk>/',views.dlP_page,name='dlproject')
]
