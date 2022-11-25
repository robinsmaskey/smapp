from django.urls import path
from .views import *
from django.contrib.auth.views import *

urlpatterns = [
    path('', get_all_posts, name='all-posts'),
    path('user/<str:profile_id>/', get_my_posts, name='logged in user posts'),
    path('<str:post_id>/comments/', get_post_comments, name='post comments'),
    path('add/', create_post, name='add post'),
    # path('<str:post_id>/update/', update_post, name='update_post'),
    path('<str:post_id>/delete/', delete_post, name='delete_post'),
    path('<str:post_id>/comment/add/', create_comment, name='add comment'),
    path('<str:post_id>/like/', add_like_to_post, name='add comment'),

]



