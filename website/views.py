from django.shortcuts import render, redirect
# to login and logout and register user libriaries
from django.contrib.auth import authenticate, login, logout
# popup messages when user login or loog out or register
from django.contrib import messages

# Create your views here.
def home(request):
    #  Check to see if user is loggin in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Autheticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There was an erro loggin in, Please try again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})