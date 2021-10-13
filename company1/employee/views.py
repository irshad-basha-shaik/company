from django.shortcuts import render
from django.http import HttpRequest
from . models import Employee
# Create your views here.

def index(request):
    return render(request,"index.html")
def home(request):
    return render(request,"home.html")
def save(request):
    res = Employee.objects.all()
    if request.method=="POST":
        reg = Employee(email=request.POST['email'],name=request.POST['name'], contact=request.POST['contact'])
        reg.save()
        return render(request,"lob.html",{"form_list": res})


def edit(request):
    id = request.GET['id']
    d = Employee.objects.get(id=id)
    return render(request,"edit.html",{"form":d})

def editform(request):
    res = Employee.objects.all()
    d = Employee.objects.filter(id=request.POST['id']).update(email=request.POST['email'],name=request.POST['name'],contact=request.POST['contact'])
    return render(request,"lob.html",{"form_list": res})
def delete(request):
    res = Employee.objects.all()
    id = request.GET['id']
    d = Employee.objects.filter(id=request.GET['id']).delete()
    return render(request, "lob.html",{"form_list":res})