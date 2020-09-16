from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView



def home(request):
    return render(request, 'blog/home.html')

def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post

def about(request):
    return  render(request, 'blog/about.html', {'title': 'Sobre BIMER'} )

