from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('band_list/', views.band_list, name='band_list'),
    path('<int:pk>/', views.band_detail, name='band_detail'),
]