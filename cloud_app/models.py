from djongo import models
from django.utils import timezone
from django.conf import settings

# from django import forms


# Create your models here.

class UserInfo(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    images = models.TextField()
    phone_num = models.CharField(max_length=15)


class FileDetailInfo(models.Model):
    _id = models.ObjectIdField()
    file_title = models.CharField(max_length=50)
    file_upload = models.DateField(default=timezone.now)
    file_url = models.FileField(upload_to='directory/')
    owner_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=50)
    # comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    # comment_name = models.CharField(max_length=50)
    # comment_date = models.DateField()
    # comment_text = models.TextField()
    # comment = models.ArrayField(
    #     model_container=Comment,
    #     # model_form_class=CommentForm
    # )

    def __str__(self):
        return self.file_title


class Comment(models.Model):
    file_detail = models.ForeignKey(FileDetailInfo, related_name='comments', on_delete=models.CASCADE)
    comment_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_date = models.DateField(default=timezone.now)
    comment_text = models.TextField()
    #     class Meta:
    #     abstract = True

    def __str__(self):
        return self.comment_name

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('comment_name', 'comment_date', 'comment_text')
