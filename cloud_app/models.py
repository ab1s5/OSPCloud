from djongo import models
# from django import forms


# Create your models here.

# class Comment(models.Model):
#     comment_name = models.CharField(max_length=50)
#     comment_date = models.DateField()
#     comment_text = models.TextField()

#     class Meta:
#         abstract = True

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('comment_name', 'comment_date', 'comment_text')


class UserInfo(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    images = models.TextField()
    phone_num = models.CharField(max_length=15)


class FileDetailInfo(models.Model):
    _id = models.ObjectIdField()
    file_title = models.CharField(max_length=50)
    file_upload = models.DateField()
    file_images = models.TextField()
    file_url = models.FileField(upload_to='directory/')
    owner_name = models.CharField(max_length=50)
    guest_name = models.CharField(max_length=50)
    comment_name = models.CharField(max_length=50)
    comment_date = models.DateField()
    comment_text = models.TextField()
    # comment = models.EmbeddedField(
    #     model_container=Comment,
    #     model_form_class=CommentForm
    # )

