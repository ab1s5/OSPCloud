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


class UserInfo(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    images = models.CharField(max_length=300)
    phone_num = models.CharField(max_length=15)

class FileDetailInfo(models.Model):
    _id = models.ObjectIdField()
    file_title = models.CharField(max_length=50)
    file_upload = models.DateField
    owner = models.EmbeddedField(
        model_container=Owner
    )
    guest = models.EmbeddedField(
        model_container=Guest
    )
    comment = models.CharField(max_length=50)
