from djongo import models
from django.utils import timezone

# from django import forms


# Create your models here.

class UserInfo(models.Model):
    # _id = models.ObjectIdField(unique=True)
    id = models.IntegerField(primary_key=False)
    name = models.CharField(max_length=50)
    email = models.CharField(primary_key=True, max_length=30, unique=True)
    phone_num = models.CharField(max_length=15)
   
    objects = models.DjongoManager()

    def __str__(self):
        return self.name

class FileDetailInfo(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    file_title = models.CharField(max_length=50)
    file_upload = models.DateField(default=timezone.now)
    file_url = models.FileField(upload_to='directory/')
    owner_name = models.ForeignKey('UserInfo', to_field='email', on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=50, null=True)
    # comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    # comment_name = models.CharField(max_length=50)
    # comment_date = models.DateField()
    # comment_text = models.TextField()
    # comment = models.ArrayField(
    #     model_container=Comment,
    #     # model_form_class=CommentForm
    # )

    objects = models.DjongoManager()

    def __str__(self):
        return self.file_title


class Comment(models.Model):
    file_detail = models.ForeignKey('FileDetailInfo', to_field='id', on_delete=models.CASCADE)
    comment_name = models.ForeignKey('UserInfo', to_field='email', on_delete=models.CASCADE)
    comment_date = models.DateField(default=timezone.now)
    comment_text = models.TextField(null=False)
    #     class Meta:
    #     abstract = True

    objects = models.DjongoManager()

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('comment_name', 'comment_date', 'comment_text')
