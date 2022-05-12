from djongo import models
# Create your models here.

class Owner(models.Model):
    _id = models.ObjectIdField()
    owner_name = models.CharField(max_length=50)

    class Meta:
        abstract = True

class Guest(models.Model):
    _id = models.ObjectIdField()
    guest_name = models.CharField(max_length=50)

    class Meta:
        abstract = True

class Comment(models.Model):
    _id = models.ObjectIdField()
    comment_name = models.CharField(max_length=50)
    comment_date = models.DateField()

    class Meta:
        abstract = True


class UserInfo(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    images = models.CharField()
    phone_num = models.Charfield(max_length=15)

class FileDetailInfo(models.Model):
    _id = models.ObjectIdField()
    file_title = models.CharField(max_length=50)
    file_upload = models.DateField()
    file_images = models.CharField()
    owner = models.EmbeddedField(
        model_container=Owner
    )
    guest = models.EmbeddedField(
        model_container=Guest
    )
    comment = models.EmbeddedField(
        model_container=Comment
    )
