

from django.shortcuts import redirect, render
from . import urls
from crudapp.models import Employees


def Index(request):
    emp = Employees.objects.all()

    context = {

        'emp':emp
    }
    return render(request, 'index.html',context)
    

def Add(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        Address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            name=name, email=email, Address=Address, phone=phone)
        emp.save()
        return redirect('home')


    return render(request, 'index.html')

def Edit(request):

    emp = Employees.objects.all()

    context = {
        'emp': emp ,
    }
    return redirect(request, 'index.html',context)

def Update(request,id):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        Address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
        id = id, name=name, email=email, Address=Address, phone=phone)
        
        emp.save()
        return redirect('home')
        

    return redirect(request, 'index.html')

def Delete(request,id):

    emp = Employees.objects.filter( id = id ).delete()

    context = {
        'emp': emp,
    }
    return redirect('home')

    