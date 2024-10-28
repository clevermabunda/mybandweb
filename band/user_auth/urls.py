from django.urls import path
from . import views
from .views import SignUpView

app_name = 'user_auth'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('show_user/', views.show_user, name='show_user'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path("signup/", SignUpView.as_view(), name="signup"),
]

"""
URL configuration for the user authentication app.

This module defines the URL patterns for user login, user display, user authentication,
and user registration (sign-up) within the user_auth application.

Patterns:
- login: The main login page.
- show_user: A page displaying the logged-in user's information.
- authenticate_user: Endpoint for processing user login authentication.
- signup: A page for user registration using a sign-up form.
"""
