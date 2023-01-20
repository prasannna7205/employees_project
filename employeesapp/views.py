from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import employees
import faker
fake=faker.Faker()

def generatingData(request):
    for i in range(100):
        employees(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(), 
        company=fake.random_element(elements=('TCS','WIPRO','INFOSYS','CTS')),
        salary=fake.random_element(elements=(10000,20000,300000,40000)),
        address=fake.random_element(elements=('hyderabad','chennai','bangolre','pune'))
        ).save()
    return HttpResponse('data save')
def featchingData(request):
    emps=employees.objects.all()
    return render(request,'featchingData.html',{'emps':emps})
def hyderabad(request):
    if request.method == 'GET':
        emps=employees.objects.filter(address='hyderabad')
        return render(request,'hydData.html',{'emps':emps})
    else:
        com=request .POST['data']
        emps=employees.objects.filter(address='hyderabad' )& employees.objects.filter(company=com )
        return render (request,'hydData.html',{'emps':emps})
def bangalore(request):
    emps=employees.objects.filter(address='bangolre')
    return render(request,'bangData.html',{'emps':emps})
def chennai(request):
    emps=employees.objects.filter(address='chennai')
    return render(request,'cheData.html',{'emps':emps})

def pune(request):
    emps=employees.objects.filter(address='pune')
    return render(request,'puneData.html',{'emps':emps})
def homepage(request):
    return render(request,'homepage.html')




