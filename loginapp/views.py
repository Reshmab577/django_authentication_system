from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import signup



# Create your views here.
def home(request):
   return render(request,'loginapp/home.html')
def signin(request):
   if request.method == "POST":
      username = request.POST.get('username')
      password = request.POST.get('pass1')
      try:
         upintable=signup.objects.get(username=username,pass1=password)
         request.session['una']=username
         #return render(request,'loginapp/home.html')
         return redirect('home')
      except signup.DoesNotExist:
         return redirect('signup')
   return render(request,'loginapp/signin.html')
def signup_save(request):
   if request.method == "POST":
      username = request.POST.get('username')
      alreadyexist=signup.objects.filter(username=username)
      if alreadyexist:
         return redirect('home')
      firstname = request.POST.get('firstname')
      secondname = request.POST.get('secondname')
      email = request.POST.get('email')
      pass1 = request.POST.get('pass1')
      pass2 = request.POST.get('pass2')
      print(username)
      signup(username=username,firstname=firstname,secondname=secondname,email=email,pass1=pass1,pass2=pass2).save()
      # return render('signup')
      
   return render(request,'loginapp/signup.html')
def signout(request):
   return render(request,'loginapp/signout.html')

