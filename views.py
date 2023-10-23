from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "invalid password")
           # return HttpResponse("username or password is not matched")
    return render(request, 'login.html')

def SignupPage(request):
    if request.method=='POST':
        user_name=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            messages.info(request, "password does not match")
            #return HttpResponse("password does not match !!!")
        else:
            my_user=User.objects.create_user(user_name,email,pass1)
            my_user.save()
            return redirect('login')
           
            #return HttpResponse("created!!!!!")

        
    return render(request, 'signup.html')

def Logout(request):
    logout(request)
    return redirect('login')
    


