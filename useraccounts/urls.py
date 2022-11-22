from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_user,  name='register-user'),
    # path('login/', ),
    # path('logout/',),
    # path('update-profile', 'update-profile'),
]