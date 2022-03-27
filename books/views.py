from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import redirect, render
from .models import*
from django.contrib.auth.models import User

# Create your views here.
def profil_unik(request):
    return render(request,'books/profile_unik.html')


def ranking(request):
    return render(request,'books/index.html')

def profile(request):
    return render(request,'books/profile.html')

def signin(request):
    if request.POST.get("signin"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser == True:
                return redirect('moderator/')
            else:
                return redirect('main/')
        
    return render(request,'books/signin.html')

def signup(request):
    if request.POST.get("signup"):

        acc = Account.objects.create(email=request.POST.get("email"),password=request.POST.get("password"),first_name=request.POST.get("name"),last_name=request.POST.get("last_name"),phone_number=request.POST.get("phonw"),id_number=request.POST.get("id_num"),library_id=Library(id=1),date_joined='2021-03-27',last_login='2021-03-27',is_admin=False,is_active=True,is_librarian=False,is_premium=True,is_staff=False,is_superuser=False)
        user = User.objects.create(username=request.POST.get("id_num"),first_name=request.POST.get("name"),last_name=request.POST.get("last_name"),password=request.POST.get("password"))
    return render(request,'books/signup.html')

def books(request):
    return render(request,'books/books.html')

def korzina(request):
    return render(request,'books/korzina.html')
def listq(request):
    return render(request,'books/list.html')
def main(request):
    return render(request,'books/main.html')
def payment(request):
    return render(request,'books/payment.html')
def zakazy(request):
    return render(request,'books/zakazy.html')
def reg_book(request):
    return render(request,'books/reg_book.html')
def moderator(request):
    return render(request,'books/moderator.html')