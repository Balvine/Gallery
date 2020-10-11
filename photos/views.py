
from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
# from .models import Image

# Create your views here.
def photos(request):
    # images = Image.all_images()
    return render(request, 'index.html')
