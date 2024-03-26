from django.urls import path
from users import views

urlpatterns = [
    path("signup/", views.register, name='register'),
     path("profile/", views.profile, name='profile'),
]