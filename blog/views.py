from typing import Any
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView


def get_date(post):
    return post['date']

# Create your views here.


class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


# def starting_page(request):
#     # Django will read the whole line, then making the query to the database, so the query will only take 3 latest date post in the database, so the performance is better, because it only fetches 3 results from the database, and because the [-3:] is not supported by django
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#         "all_posts": all_posts,
#     })


class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["post_tags"] = self.object.tags.all()
        return context

# def post_detail(request, slug):
#     # all_posts = Post.objects.all()
#     # identified_post = next(
#     #     post for post in all_posts if post.slug == slug)
#     identified_post = get_object_or_404(Post, slug=slug)

#     return render(request, "blog/post-detail.html", {
#         "post": identified_post,
#         "post_tags": identified_post.tags.all()
#     })
