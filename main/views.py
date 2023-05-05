from django.shortcuts import render
from .models import BlogIndexPage
# Create your views here.

def home(request):
    b = BlogIndexPage.objects.live()
    return render(request, "index.html", {'page': b[0]})

def blog(request):
    return render(request, 'blog.html')