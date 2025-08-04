from django.shortcuts import render
from .models import Author, Post, Tag

ALL_POSTS = Post.objects.all()


def get_date(post):
    return post.get('date')


def starting_page(request):
    sorted_posts = sorted(ALL_POSTS, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html",
                  {"posts": latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html",
                  {"all_posts": ALL_POSTS})


def post_detail(request, slug):
    identified_post = next(post for post in ALL_POSTS if post["slug"] == slug)
    return render(request, "blog/post-detail.html",
                  {"post": identified_post})
