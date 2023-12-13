from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .models import Post
from django.contrib.auth.models import User

from django.db.models import Q
from django.contrib.staticfiles.views import serve

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


# Create your views here.
def home(request):
    template = "blog/home.html"

    context = {"posts": Post.objects.all()}

    return render(request, template, context)


def search(request):
    template = "blog/home.html"

    query = request.GET.get("q")

    result = Post.objects.filter(
        Q(title__icontains=query)
        | Q(author__username__icontains=query)
        | Q(content__icontains=query)
    )
    context = {"posts": result}

    return render(request, template, context)


def getFile(request):
    return serve(request, "File")


def about(request):
    return render(request, "blog/about.html", {"title": "About"})


def blog_list(request):
    return render(request,"blog/blog_list.html" )


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 2


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"

    paginate_by = 2

    def get_queryset(self) -> QuerySet[Any]:
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    success_url = "/post/home/"
    template_name = "blog/post_form.html"
    fields = ["title", "content", "file"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    success_url = "/post/home/"
    template_name = "blog/post_form.html"
    fields = ["title", "content", "file"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    success_url = "/post/home/"
    template_name = "blog/post_confirm_delete.html"
