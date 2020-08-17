from django.shortcuts import render

from .models import RegistrationData
from .forms import RegistrationForm,LoginForm
from django.http.response import HttpResponse

def registration_view(request):
    if request.method == "POST":
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            rform.save()
            # first_name = request.POST.get('first_name')
            # last_name = request.POST.get('last_name')
            # username = request.POST.get('username')
            # password = request.POST.get('password')
            # email = request.POST.get('email')
            # mobile = request.POST.get('mobile')
            # data = RegistrationData(
            #     first_name=first_name,
            #     last_name=last_name,
            #     username=username,
            #     password=password,
            #     email=email,
            #     mobile=mobile
            # )
            # data.save()
            lform=LoginForm()
            return render(request,'login-page.html',{'lform':lform})
        else:
            return HttpResponse("User Invalid Data")
    else:
        rform = RegistrationForm()
        return render(request,'reg-page.html',{'rform':rform})

def login_view(request):
    if request.method == "POST":
        lform=LoginForm(request.POST)
        if lform.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            uname=RegistrationData.objects.filter(username=username)
            pwd=RegistrationData.objects.filter(password=password)
            if uname and pwd:
                return HttpResponse('Login Successful')
            else:
                return HttpResponse('Login Failed Please Enter Your Correct Details Again')
    else:
        lform=LoginForm()
        return render(request, 'login-page.html', {'lform':lform})







