from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from app.models import *
# Create your views here.
def School_Data(request):
    ESFO=School()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=School(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['Sname']
            sp=SFDO.cleaned_data['Sprincipal']
            sl=SFDO.cleaned_data['Slocation']
            SO=Create_School.objects.get_or_create(Sname=sn,Sprincipal=sp,Slocation=sl)[0]
            SO.save()
            



            
        else:
            return HttpResponse('Not a Valid Data')

    return render(request,'school_creation.html',d)