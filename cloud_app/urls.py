from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from cloud_app import views

urlpatterns = [
    path('', views.main, name='main'),
    path('useredit', views.user_edit, name='user_edit'),
    path('fileupload', views.file_upload, name='file_upload'),
    path('detail/<int:pk>', views.file_detail, name='file_detail'),
    path('edit/<int:pk>', views.file_edit, name='file_edit'),
    path('remove/<int:pk>', views.file_remove, name='file_remove'),
    path('commentadd/<int:pk>', views.add_comment, name='add_comment'),
    path('removecom/<int:pk>', views.remove_comment, name='remove_comment'),
    path('commentedit', views.comment_edit, name='comment_edit'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.sign_up, name='sign_up'),
]