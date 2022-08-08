from post.views import index, newPost, postDetails, tags, like, favorite
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('dodaj_post/', newPost, name='newPost'),
    path('<uuid:post_id>', postDetails, name='postDetails'),
    path('tag/<slug:tag_slug>', tags, name='tags'),
    path('<uuid:post_id>/polubienie', like, name='like'),
    path('<uuid:post_id>/ulubione', favorite, name='favorite'),

]