from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def emp(request):
    empno=input('enter empno  :')
    ename=input('enter ename  :')
    job=input('enter job  :')
    mgr=input('enter mgr  :')
    hiredate=input('enter hiredate :')
    sal=input('enter sal :')
    comm=input('enter comm :')
    deptno=input('enter deptno :')

    EO=Employe.objects.get_or_create(empno=empno,ename=ename,job=job,mgr=mgr,hiredate=hiredate,sal=sal,comm=comm,deptno=deptno)[0]
    EO.save()
    return HttpResponse('employe table')


def employe(request):
    eo=Employe.objects.all()
    d={'details':eo}
    return render(request,'employe.html',d)