from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.logout, name='logout'),
]