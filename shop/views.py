from django.shortcuts import render
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages


def allprodcat(request):
    c = Category.objects.all()
    return render(request,'category.html',{'c':c})

def allproducts(request,p):
    c = Category.objects.get(slug=p)
    p = Product.objects.filter(category__slug=p)
    return render(request,'product.html',{'p':p,'c':c})

def details(request,d):
    b=Product.objects.get(slug=d)
    return render(request,'details.html',{'b':b})

def register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        cp = request.POST['cp']
        if p==cp:
         user = User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
         user.save()
        return user_login(request)
    return render(request,'register.html')

def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return allprodcat(request)
        else:
            messages.error(request,"Invalid credentials")
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return allprodcat(request)
