from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

def post_detail(request, id):
    # try:
    #     post = Post.objects.get(pk=id)
    # except Post.DoesNotExist:
    #     raise Http404("Post does not exist")
    post = get_object_or_404(Post, pk=id, status=Post.Status.PUBLISHED)

    return render(request,
                  'blog/post/detail.html',
                  {'post': post})