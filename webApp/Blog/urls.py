from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from . import views

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

urlpatterns = [

    # path('', views.home, name='blog-home'),
    path('search/',views.search,name='search' ),
    path('about/', views.about, name='blog-about'),
    
    path('post/home/', PostListView.as_view(), name='blog-home'),
    path('post/new/',PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)