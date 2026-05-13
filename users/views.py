from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
from .forms import UserCreationForm,UserLoginForm
from django.contrib.auth import authenticate,login
 
def register(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
        return HttpResponse("Registration successful")
    return render(request,'users/register.html',{'form':form})

def user_login(request):
    form=UserLoginForm()
    if request.method == 'POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponse("Login successful")
            else:
                return HttpResponse("Invalid credentials")
    return render(request,'users/login.html',{'form':form})
		
	
			
    