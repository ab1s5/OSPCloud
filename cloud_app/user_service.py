import pymongo
from pymongo import MongoClient

client = MongoClient('35.160.38.122')
# username = 'root'
# password = 'ospcloud0519'
# connection = pymongo.MongoClient(host='35.160.38.122', port=27017, username='root', password='ospcloud0519')

db = client.admin

posts = db.UserInfo

post = {
    "name" : "test",
    "email" : "aaa@aaa.com",
    "images" : "aaaaaaa",
    "phone_num" : "010-1111-1111"
}

posts.insert_one(post)

# class UserInfo(models.Model):
#     _id = models.ObjectIdField()
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=30)
#     images = models.TextField()
#     phone_num = models.CharField(max_length=15)
