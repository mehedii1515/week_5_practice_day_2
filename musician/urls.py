from django.urls import path
from . import views

urlpatterns = [
    # path('add/', views.add_musician, name='add_musician'),
    # path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='user_login'),
    # path('logout/', views.user_logout, name='user_logout'),
    path('add/', views.AddMusicianCreateView.as_view(), name='add_musician'),
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
]