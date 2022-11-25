from django.urls import path
from .views import *
from django.contrib.auth.views import *

urlpatterns = [
    path('', get_all_posts, name='all-posts'),
    path('user/<str:profile_id>/', get_my_posts, name='logged in user posts'),
]



