from django.urls import path
from . import views
from .views import SignUpView

app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('show_user/', views.show_user, name= 'show_user'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path("signup/", SignUpView.as_view(), name="signup"),
]
