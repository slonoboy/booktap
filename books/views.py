from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import redirect, render
from .models import*
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def profil_unik(request):
    if request.POST.get("logout"):
        logout(request)
        return redirect('/')
    return render(request,'books/profile_unik.html')

@login_required(login_url='/')
def ranking(request):
    if request.POST.get("logout"):
        logout(request)
        return redirect('/')
    return render(request,'books/index.html')

@login_required(login_url='/')
def profile(request):
    userr = Account.objects.filter(id_number=request.user.username)
    context = { 
        "userr" : userr
    }
    if request.POST.get("logout"):
        logout(request)
        return redirect('/')
    return render(request,'books/profile.html',context=context)

def signin(request):
    
    if request.POST.get("signin"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser == True:
                return redirect('moderator/')
            if request.user.is_staff==True:
                return redirect('reg_book/')
            else:
                return redirect('main/')
        
    return render(request,'books/signin.html')
@login_required(login_url='/')
def signup(request):
    if request.POST.get("signup"):
        user = User.objects.create_user(username=request.POST.get("id_num"),first_name=request.POST.get("name"),last_name=request.POST.get("last_name"),password=request.POST.get("password"))
        user.save()
        acc = Account.objects.create(email=request.POST.get("email"),password=request.POST.get("password"),first_name=request.POST.get("name"),last_name=request.POST.get("last_name"),phone_number=request.POST.get("phonw"),id_number=request.POST.get("id_num"),library_id=Library(id=1),date_joined='2021-03-27',last_login='2021-03-27',is_admin=False,is_active=True,is_librarian=False,is_premium=True,is_staff=False,is_superuser=False)
    return render(request,'books/signup.html')
@login_required(login_url='/')
def books(request):
    if request.POST.get("logout"):
        logout(request)
        return redirect('/')
    return render(request,'books/books.html')
@login_required(login_url='/')
def korzina(request):
    if request.POST.get("logout"):
        logout(request)
        return redirect('/')
    return render(request,'books/korzina.html')
@login_required(login_url='/')
def listq(request):
    if request.POST.get("logout"):
        logout(request)
        return redirect('/')
    return render(request,'books/list.html')
@login_required(login_url='/')
def main(request):
    if request.POST.get("logout"):
        logout(request)
        return redirect('/')
    return render(request,'books/main.html')
@login_required(login_url='/')
def payment(request):
    if request.POST.get("logout"):
        logout(request)
        return redirect('/')
    return render(request,'books/payment.html')
@login_required(login_url='/')
def zakazy(request):
    if request.POST.get("logout"):
        logout(request)
        return redirect('/')
    return render(request,'books/zakazy.html')
@login_required(login_url='/')
def reg_book(request):
    if request.POST.get("logout"):
        logout(request)
        return redirect('/')
    if request.POST.get("subm_book"):
        book_name = request.POST.get("book_name")
        author = request.POST.get("author")
        genre = request.POST.get("genre")
        opisanie = request.POST.get("opisanie")
        file = request.FILES["myFile"]
        file_name = default_storage.save(file.name,file)
        file_url = default_storage.path(file_name)
        book = Book.objects.create(book_name = book_name, author = author, description = opisanie, genres = genre, image = file_url )


    return render(request,'books/reg_book.html')
@login_required(login_url='/')
def moderator(request):
    if request.POST.get("logout"):
        logout(request)
        return redirect('/')
    return render(request,'books/moderator.html')