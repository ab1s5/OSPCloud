# from django import forms

from djongo import models
from django.utils import timezone

# Create your models here.

class UserInfo(models.Model):
    _id = models.ObjectIdField(unique=True)
    name = models.CharField(max_length=50)
    email = models.CharField(primary_key=True, max_length=30, unique=True)
    phone_num = models.CharField(max_length=15)
   
    object = models.DjongoManager()

    def __str__(self):
        return self.name

class FileDetailInfo(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    file_title = models.CharField(max_length=50)
    file_upload = models.DateField(default=timezone.now)
    file_url = models.FileField(upload_to='directory/')
    owner_name = models.ForeignKey('UserInfo', to_field='email', on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=50, null=True)

    object = models.DjongoManager()

    def __str__(self):
        return self.file_title


class Comment(models.Model):
    file_detail = models.ForeignKey('FileDetailInfo', to_field='id', on_delete=models.CASCADE)
    comment_name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment_date = models.DateField(default=timezone.now)
    comment_text = models.TextField(null=False)

    object = models.DjongoManager()