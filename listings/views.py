from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .models import Property

def sign_up(request):
    return render(request, 'listings/signup.html')

def log_in(request):
    return render(request, 'listings/login.html')

def home(request):
    properties = Property.objects.all()
    return render(request, 'listings/home.html', {'properties': properties})

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone_number = form.cleaned_data.get('phone_number')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to home after successful sign-up
    else:
        form = SignUpForm()
    return render(request, 'listings/signup.html', {'form': form})


