from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['date_added']

from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def view_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if comment.user:
        author_name = comment.user.username
        author_email = comment.user.email
    else:
        author_name = "Anonymous"
        author_email = ""
    
    response = f"Comment ID: {comment.id}<br>"
    response += f"Author: {author_name}<br>"
    response += f"Author Email: {author_email}<br>"
    response += f"Body: {comment.body}<br>"
    
    return HttpResponse(response)