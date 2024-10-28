from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
            )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('band_list')
            )
    
def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
        })   

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("user_auth:login")
    template_name = "authentication/signup.html"         
