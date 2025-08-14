from django.shortcuts import render
from .forms import *
# Create your views here.
def landingpage(req):
    return render(req,'landing.html')

def home(req):
    return render(req,'home.html')


def about(req):
    return render(req,'about.html')

def contact(req):
    return render(req,'contact.html')

def register(req):
    return render(req,'register.html')

def login(req):
    return render(req,'login.html')



def home(request):
    l=[2,3,4,5,6]
    return render(request,'home.html',{'data':l})

def landingpage(req):
    if req.method=='POST':
        form =studentform(req.POST,req.FILES)
        print(form)
        if form. is_valid():
            form.save()
            fm = studentform()
    fm = studentform()
    return render(req,'landing.html',{'fm':fm})


def login(req):
    if req.method=='POST':
        form =loginform(req.POST,req.FILES)
        

        
        if form. is_valid():
             n=form.cleaned_data['name']
             e=form.cleaned_data.get('email')
             i=form.cleaned_data.get('image')
             r= form.cleaned_data['resume']
            form.save()
           
    fm = loginform()
    return render(req,'login.html',{'fm':fm})
