from django.shortcuts import render, get_object_or_404
from .models import Band
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'band/homeband.html')\
    
@login_required(login_url="user_auth:login")
def band_list(request):
    list_of_bands = Band.objects.all()
    context = {'list_of_bands': list_of_bands}
    return render(request, 'band/bandlist.html', context)

def band_detail(request, pk):
    band = get_object_or_404(Band, pk=pk)
    context = {'band': band}
    return render(request, 'band/bandDetail.html', context)