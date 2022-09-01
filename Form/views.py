from django.shortcuts import render
from service.models import Service

def home(request):
    if request.method == "GET":
        pdata = {
            'programmer': 'Suvendu Chowdhury',
            'use': 'Django',
        }
        return render(request,'index.html',pdata)

    if request.method == "POST":
        name=request.POST.get('name','default')
        roll=request.POST.get('roll','default')
        reg=request.POST.get('reg','default')
        email=request.POST.get('email','default')

        en=Service(name=name,roll=roll,reg=reg,email=email)
        en.save()

        cdata = {
            'programmer': 'Suvendu Chowdhury',
            'use': 'Django',
            'name':name,
            'roll':roll,
            'reg':reg,
            'email':email,
        }

        return render(request,'index.html',cdata)

def table(request):
    serviceData=Service.objects.all()
    pdata = {
        'programmer': 'Suvendu Chowdhury',
        'use': 'Django',
        'serviceData': serviceData,
    }
    return render(request,'table.html',pdata)

