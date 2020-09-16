from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'blog/home.html')

def blog(request):
    return render(request, 'blog/blog.html')

def about(request):
    return  render(request, 'about.html')