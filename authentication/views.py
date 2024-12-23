from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # Or use CustomLoginForm



def login_view(request):

    print('In login_view func\n')
    if request.user.is_authenticated:
        return redirect('dashboard')

    print('In login_view func x2\n')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Or use CustomLoginForm
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('dashboard')  # Redirect to a dashboard or homepage
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid form submission.")
    else:
        form = AuthenticationForm()  # Or use CustomLoginForm


    print(request)
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')