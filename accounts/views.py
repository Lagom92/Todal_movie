from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:main')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:main')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/forms.html',{'form':form})
    
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:main')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:main')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/forms.html', {'form': form})
    
def logout(request):
    auth_logout(request)
    return redirect('movies:main')