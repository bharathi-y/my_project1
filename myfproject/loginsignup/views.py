from django.shortcuts import render,HttpResponse

# Create your views here.
def home_page(request):
    return render(request,'home_page.html',context={})
def login_page(request):
    return render(request ,'login_page.html',context={})
def signup_page(request):
    return render(request,'signup_page.html',context={})


