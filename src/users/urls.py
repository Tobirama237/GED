from django.urls import path
from .import views

urlpatterns = [
    #path for login
    path('login/', views.loginUser, name="login"),
    #path for logout
    path('logout/', views.logoutUser, name="logout"),
    #path for registering a user
    path('register/', views.registerUser, name="register"),

    #path to have profiles
    path('', views.profiles, name="profiles" ),
    #path to have profile detail
    path('profile/<str:pk>', views.userProfile, name="user-profile" ),
    #path to have user account
    path('account/', views.userAccount, name="user-account" ),
]