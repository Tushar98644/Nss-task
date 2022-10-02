from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages 


def register(request):
   if request.method=='POST':
     username=request.POST['username']
     password=request.POST['password']

     user=authenticate(request,username=username,password=password)

     if user != None:
      login(request,user)
      messages.success(request,"valid cerendtials")
      return redirect('https://www.iitg.ac.in/nss/')
        
     

     else:
      messages.error(request,"bad cerendtials")
      return redirect('/login')

   return render (request,'login.html')
    
