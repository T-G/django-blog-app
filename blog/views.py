from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required

from .models import Post
from .forms import PostForm, PostDeleteForm

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {'page':'home', 'posts': posts}
    return render(request, 'home.html', context)

def detail(request, slug=None):
    
    post = get_object_or_404(Post, slug=slug)

    context = {'page': 'blog_detail', 'post': post}
    
    return render(request, 'blog/detail.html', context)

@permission_required('blog.add_post', raise_exception=True)
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    context = {'page': 'blog_create', 'form': form,}
    return render(request, 'blog/create.html', context)   

@permission_required('blog.change_post', raise_exception=True)
def edit(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
        context = {
            'page' : 'blog_edit',
            'form' : form,
            'post' : post
        }
        return render(request, 'blog/edit.html', context)

@permission_required('blog.delete_post', raise_exception=True)
def delete(request, pk=None):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostDeleteForm(request.POST, instance=post)
        if form.is_valid():
            post.delete()
            return redirect('home')
    else:
        form = PostDeleteForm(instance=post)
    context = {
        'page' : 'blog_delete',
        'form' : form,
        'post' : post,
    }
    return render(request, 'blog/delete.html', context)
