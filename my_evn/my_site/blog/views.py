from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm
# Create your views here.


def frontpage(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "frontpage.html", context)


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save

            return redirect('blog:detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, "pst_detail.html", {"post": post, "form": form})
