from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, PropertyAddForm  # Import both forms
from .models import Property

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

def log_in(request):
    return render(request, 'listings/signup.html')

def property_add(request):
    if request.method == 'POST':
        form = PropertyAddForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.user = request.user  # Attach the current user to the property
            property.save()
            return redirect('home')  # Redirect to home after property is added
    else:
        form = PropertyAddForm()  # Use PropertyAddForm here, not SignUpForm
    return render(request, 'listings/property_add.html', {'form': form})


def home(request):
    properties = Property.objects.all()
    return render(request, 'listings/home.html', {'properties': properties})
