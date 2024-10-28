from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

def user_login(request):
    """
    Render the login page for users.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: The rendered login page.
    """
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    """
    Authenticate a user based on provided username and password.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponseRedirect: Redirects to the login page if authentication fails,
                          or to the band list if successful.
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    
    if user is None:
        return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('band_list'))

def show_user(request):
    """
    Render the user page displaying the logged-in user's information.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: The rendered user page with the username.
    """
    print(request.user.username)  # Consider removing this in production
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password  # Note: Avoid exposing passwords!
    })

class SignUpView(generic.CreateView):
    """
    View for user sign-up.

    This view handles the user registration process using Django's UserCreationForm.

    Attributes:
    form_class (UserCreationForm): The form class used for user registration.
    success_url (str): The URL to redirect to upon successful registration.
    template_name (str): The template to use for rendering the sign-up page.
    """
    
    form_class = UserCreationForm
    success_url = reverse_lazy("user_auth:login")
    template_name = "authentication/signup.html"
