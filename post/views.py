from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

import post.models
from post.models import Post, Stream, Tag, Likes
from post.forms import NewPostForm
from authy.models import Profile
from comment.models import Comment
from comment.forms import CommentForm


# Create your views here.

@login_required
def index(request):
    user = request.user
    posts = Stream.objects.filter(user=user)
    group_ids = [post.post_id for post in posts]
    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
    context = {'post_items': post_items}
    return render(request, 'index.html', context)


@login_required
def newPost(request):
    user = request.user.id
    form = NewPostForm()
    tags_objs = []

    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            caption = form.cleaned_data.get('caption')
            tags_form = form.cleaned_data.get('tags')

            tags_list = list(tags_form.split(','))

            for tag in tags_list:
                t, created = Tag.objects.get_or_create(title=tag)
                tags_objs.append(t)
            p, created = Post.objects.get_or_create(picture=picture, caption=caption, user_id=user)
            p.tags.set(tags_objs)
            p.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'new_post.html', context)


@login_required
def postDetails(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    favorited = False
    comments = Comment.objects.filter(post=post).order_by('-date')
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=user)
        if profile.favorites.filter(id=post_id).exists():
            favorited = True
    context = {'post': post, 'favorited': favorited, 'comments': comments, 'form': form}

    return render(request, 'post_detail.html', context)


@login_required
def tags(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags=tag).order_by('-posted')
    context = {'tag': tag, 'posts': posts}

    return render(request, 'tag.html', context)


@login_required
def like(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.likes
    liked = Likes.objects.filter(user=user, post=post).count()

    if not liked:
        like = Likes.objects.create(user=user, post=post)
        current_likes += 1
    else:
        Likes.objects.filter(user=user, post=post).delete()
        current_likes -= 1

    post.likes = current_likes
    post.save()

    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


@login_required
def favorite(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    profile = Profile.objects.get(user=user)

    if profile.favorites.filter(id=post_id).exists():
        profile.favorites.remove(post)
    else:
        profile.favorites.add(post)
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
