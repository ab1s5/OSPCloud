import pymongo
from pymongo import MongoClient

client = MongoClient('35.160.38.122')
db = client.admin

posts = db.FileDetailInfo

post = {
    "name" : "test",
    "email" : "aaa@aaa.com",
    "images" : "aaaaaaa",
    "phone_num" : "010-1111-1111"
}

posts.insert_one(post)

# class FileDetailInfo(models.Model):
#     _id = models.ObjectIdField()
#     file_title = models.CharField(max_length=50)
#     file_upload = models.DateField()
#     file_images = models.TextField()
#     file_url = models.TextField()
#     owner = models.EmbeddedField(
#         model_container=Owner
#     )
#     guest = models.EmbeddedField(
#         model_container=Guest
#     )
#     comment = models.EmbeddedField(
#         model_container=Comment
#     )