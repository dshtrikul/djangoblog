from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView  )
from .models import Post
from .forms import PostCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    # ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostCreateForm
    model = Post

    # succsess_url = 'blog-home'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # context_object_name = 'post'

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostCreateForm
    # succsess_url = 'blog-home'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # context_object_name = 'post'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# class PostDeleteImageView(PostDeleteView):
#     success_url = '/'

def image_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.image.delete()
    return redirect(reverse('post-update', args = (pk,)))

def about(request):
    return render(request, 'blog/about.html')
