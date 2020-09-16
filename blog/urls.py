from django.urls import path
from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('blog/', PostListView.as_view(), name='blog-blog'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail')
]

