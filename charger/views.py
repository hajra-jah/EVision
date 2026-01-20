from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'charger/index.html')

@login_required
def dashboard(request):
    return render(request, 'charger/dashboard.html')

@login_required
def map_view(request):
    return render(request, 'charger/map_page.html')

@login_required
def charging_view(request):
    return render(request, 'charger/charging.html')

def about(request):
    return render(request, 'charger/about.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful! Welcome to EVision.")
            return redirect('dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = UserCreationForm()
    return render(request, 'charger/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'charger/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('login')

def calculate_charge(request):
    if request.method == "POST":
        mode = request.POST.get('mode') 
        value = float(request.POST.get('value', 0))
        rate = 50  # 1% = 50 Rs.
        current_soc = 20  # Dummy current battery percentage
        
        target_soc = 0
        total_cost = 0

        if mode == 'price':
            # Case: User ne paise bataye (e.g. 1000 Rs)
            max_percent_increase = value / rate
            target_soc = min(100, current_soc + max_percent_increase)
            total_cost = value
        else:
            # Case: User ne percentage batayi (e.g. 80%)
            target_soc = value
            if target_soc > current_soc:
                total_cost = (target_soc - current_soc) * rate
            else:
                total_cost = 0
            
        return JsonResponse({
            'target': target_soc, 
            'cost': total_cost,
            'current': current_soc
        })


