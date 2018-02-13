from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts': posts})
#def PostListView(ListView):

def post_details(request,year,month,day,post):
    post=get_object_or_404(Post, slug=post,
                           status='Published',
                           publish_year=year,
                           publish_month=month,
                           publish_day=day)
    return render(request,
                  'blog/post/details.html',
                  {'post': post})

# Create your views here.
