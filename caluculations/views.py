from django.shortcuts import render
from django.http import HttpResponse
def input(request):
    return render(request,'basicmath.html')
def caluculate(request):
    try:
        a=request.GET['t1']
        x=int(a)
        b=request.GET['t2']
        y=int(b)
        op=request.GET["operation"]
    except (ValueError):
        return render(request,'basicmath.html')
    if op=="add":
        z=x+y
        return HttpResponse("""<html><body bgcolor=green><h1>sum is:""" +str(z)+"""</h1></body></html>""")
    elif op=="sub":
        z=x-y
        return HttpResponse("""<html><body bgcolor=green><h1>subtraction is:"""+str(z)+"""</h1></body></html>""")
    elif op=="mul":
        z = x*y
        return HttpResponse("""<html><body bgcolor=green><h1>sum is:""" +str(z)+"""</h1></body></html>""")
    elif op=="div":
        try:
            z=x/y
            return HttpResponse("""<html><body bgcolor=green><h1>divison is:""" + str(z)+"""</h1></body></html>""")
        except(ZeroDivisionError):
            return HttpResponse("can not devide a number with zero")








#Create your views here.
