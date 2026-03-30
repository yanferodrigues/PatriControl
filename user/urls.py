from django.contrib import admin
from django.urls import path
from user.views import user,login_view,logout_view

urlpatterns = [
    path('usuario/', user, name="usuario"),
    path('accounts/login/', login_view, name="login"),
    path('logout/', logout_view, name="logout")
]