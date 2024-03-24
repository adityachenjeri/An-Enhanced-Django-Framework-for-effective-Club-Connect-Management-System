from django.shortcuts import render, HttpResponse
from .models import Student, Role, Department
from datetime import datetime
from django.db.models import Q

# Create your views here.

def gitam(request):
    return render(request, 'gitam.html')

def sq(request):
    return render(request, 'sq.html')


def index(request):
    return render(request, 'index.html')

def all_stu(request):
    stud = Student.objects.all()
    context = {
        'stud': stud
    }
    print(context)#dict in django, it is passed into templates
    return render(request, 'view_all_stu.html', context)

def add_stu(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        reg_num = int(request.POST['reg_num'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        new_stu = Student(first_name= first_name, last_name=last_name, dept_id = dept, reg_num=reg_num, role_id = role, phone=phone,  hire_date = datetime.now())
        new_stu.save()
        return HttpResponse('Student added Successfully')
    elif request.method=='GET':
        return render(request, 'add_stu.html')
    else:
        return HttpResponse("An Exception Occured! Student Has Not Been Added")    
    #return render(request, 'add_stu.html')

def remove_stu(request, stu_id=0):
    if stu_id:
        try:
            stu_to_be_removed = Student.objects.get(id=stu_id)
            stu_to_be_removed.delete()
            return HttpResponse("Student Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    stud = Student.objects.all()
    context = {
        'stud': stud
    }
    return render(request, 'remove_stu.html', context)

def filter_stu(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        stud = Student.objects.all()
        if name:
            stud = stud.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            stud = stud.filter(dept__name__icontains = dept)
        if role:
            stud = stud.filter(role__name__icontains = role)

        context = {
            'stud': stud
        }
        return render(request, 'view_all_stu.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_stu.html')
    else:
        return HttpResponse('An Exception Occurred')

