from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_control, never_cache
from django.contrib import messages


from .forms import UserCreateForm
# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def login_user(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.success(
                request, 'There was an error Logging, try again.')
            return redirect('login_user')

    else:
        return render(request, 'auth/authenticate/login.html')
    
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration succesful')
            return redirect('home')
    else:
        form = UserCreateForm()
    return render(request, 'auth/authenticate/register_user.html', {'form': form})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@never_cache
def log_out(request):
    logout(request)
    messages.success(request, 'You were logout')
    return redirect('login_user')