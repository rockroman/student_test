from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Post, Comment

def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'blog/frontpage.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

@login_required
def edit_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {'form': form})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.user:
        if request.method == 'POST':
            comment.delete()
            return redirect('post_detail', slug=comment.post.slug)
        return render(request, 'blog/delete_comment.html', {'comment': comment})
    else:
        return redirect('post_detail', slug=comment.post.slug)
