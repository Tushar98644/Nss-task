from urllib import request
from django.shortcuts import render,redirect
# from  django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from django.contrib.auth.models import User



def signup(request):
 
 

    if request.method == 'POST':
       username=request.POST['username']
       password=request.POST['password'] 
        
       myuser=User.objects.create_user(username = username)
       myuser.set_password(password)
       myuser.save()
       
       messages.success(request,("your account has been successfully created"))
        

       
       return redirect('/')

    
    return render(request,'signup.html')
       
     




# Create your views here.
