from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def profil_unik(request):
    return render(request,'books/profile_unik.html')


def ranking(request):
    return render(request,'books/index.html')

def profile(request):
    return render(request,'books/profile.html')

def signin(request):
    return render(request,'books/signin.html')

def signup(request):
    if request.POST.get("signin"):
        print(request.POST.get("username"))
        print(request.POST.get("password"))
        
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