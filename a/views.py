from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from datetime import timedelta
from datetime import datetime
# Create your views here.
def index(request):
    books = Book.objects.filter(is_available=True)
    if request.method=="POST":
        query = request.POST.get("query")
        books = Book.objects.filter(title__icontains=query)
        return render(request,"a/index.html",{"books":books})
    return render(request,"a/index.html",{"books":books})

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already taken")
        elif User.objects.filter(email=email).exists():
            messages.error(request,"Email already taken")
        else:
            user = User.objects.create_user(username=username,password=password,email=email)
            messages.success(request,"User created successfully")
    return render(request,"a/signup.html",{})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("index")
            else:
                messages.error(request,"Incorrect Password")
        else:
            messages.error(request,"Invalid Username")
        
    return render(request,"a/login.html",{})

def logout_user(request):
    logout(request)
    return redirect("index")

@login_required
def register(request):
    if request.method == 'POST':
        membership_type = request.POST.get('membership_type')
        end_date = now()

        if membership_type == '6 months':
            end_date += timedelta(days=6*30) 
        elif membership_type == '1 year':
            end_date += timedelta(days=12*30)
        elif membership_type == '2 years':
            end_date += timedelta(days=24*30)

        Membership.objects.create(
            user=request.user,
            end_date=end_date,
            membership_type=membership_type
        )

        return redirect('membership_thanks')  # Assuming there's a membership_thanks view

    return render(request, 'a/register.html')

def membership_thanks(request):
    return render(request, 'a/membership_thanks.html')

@login_required
def rent(request, id):
    book = Book.objects.get(id=id)
    
    issue_date = now().date()
    max_return_date = issue_date + timedelta(days=15)

    if request.method == "POST":
        return_date = request.POST.get("return_date")
        Transaction.objects.create(book=book, user=request.user, issue_date=issue_date, return_date=max_return_date,fine=0)
        book.is_available = False
        book.save()
        return redirect("successpage")
    else:
        return_date = max_return_date

    return render(request, "a/rent.html", {"book": book, "issue_date": issue_date, "return_date": return_date})

def successpage(request):
    return render(request,"a/successpage.html",{})
