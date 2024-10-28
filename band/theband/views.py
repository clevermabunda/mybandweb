from django.shortcuts import render, get_object_or_404
from .models import Band
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    """
    Render the home page for the band application.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: The rendered home page.
    """
    return render(request, 'band/homeband.html')

@login_required(login_url="user_auth:login")
def band_list(request):
    """
    Render a list of all bands.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: The rendered list of bands.

    Context:
    - list_of_bands (QuerySet): A queryset of all Band objects.
    """
    list_of_bands = Band.objects.all()
    context = {'list_of_bands': list_of_bands}
    return render(request, 'band/bandlist.html', context)

def band_detail(request, pk):
    """
    Render the details of a specific band.

    Parameters:
    request (HttpRequest): The HTTP request object.
    pk (int): The primary key of the band to retrieve.

    Returns:
    HttpResponse: The rendered details of the specified band.

    Raises:
    Http404: If the band with the given primary key does not exist.

    Context:
    - band (Band): The Band object retrieved by the primary key.
    """
    band = get_object_or_404(Band, pk=pk)
    context = {'band': band}
    return render(request, 'band/bandDetail.html', context)
