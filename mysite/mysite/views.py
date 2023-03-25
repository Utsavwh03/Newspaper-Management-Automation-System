from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from Newspaper.models import Employee,Customer
def check(requests):
    return HttpResponse("I will never give up")
def checkme(requests,idno):
    return HttpResponse(7+13)
def homepage(requests):
    customer_data=Customer.objects.all()
    # for a in employee_data:
    #     print(a.name)

    data={'title':'Check Page','hello':'Utsav','clist':['PHP','Java','Project'],
          'student_details':
          [{'name':'Pradeep','phone':'8538855325'},{'name':'utsav','phone':'580485489'}],
          'numbers':[20,30,40,50],'customer_data':customer_data
          }
    return render(requests,"index.html",data)#send data  to html page 

def addData(requests):
    empadd=Employee(name="Rohan",address="London",email="h@gmail.com",phone_number="54534534",salary="554524")
    empadd.save()
    return HttpResponse()