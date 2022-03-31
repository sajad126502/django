from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def login_view(req):
    context={}
    if(req.user.is_authenticated):
       return redirect("/logout")
    if req.method=="POST":
           username=req.POST.get("username")  
           password=req.POST.get("password")
           user=authenticate(req,username=username,password=password)
           if user is not None:
              login(req,user)
              return redirect("/admin")
           context["error"]="invalid username or password"
    return render(req,"accounts/login.html",context)


def register_view(req):
   form=UserCreationForm(req.POST or None)
   if form.is_valid():
       form.save()
       return redirect("/login")
   context={"form":form}
   return render(req,"accounts/register.html",context)

def logout_view(req):
    if(req.method=="POST"):
       print(dir(req))
       print(req.user.password)
       logout(req)
       return redirect("/login")
    return render(req,"accounts/logout.html")

