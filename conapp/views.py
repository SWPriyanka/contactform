from django.shortcuts import render
from .models import StudentData
# Create your views here.
def contactForm(request):
    if request.method=="GET":
        return render(request,"form.html")
    else:
        StudentData( 
        name=request.POST.get('name'),
        email=request.POST.get('email'),
        phonenumber=request.POST.get('phonenumber'),
        address=request.POST.get('address'),
        dob=request.POST.get('dob')
        ).save()
        return render(request,"form.html")