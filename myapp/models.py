from django.db import models
from django.core.validators import MinLengthValidator

class Posts(models.Model):
   postid = models.CharField(max_length=5500)
   post = models.CharField(max_length=5500)
   username = models.CharField(max_length=20)
   class Meta:
      db_table = "post"


class Comment(models.Model):
   postid = models.CharField(max_length=5500)
   commentid = models.CharField(max_length=5500)
   comment = models.CharField(max_length=5500)
   username = models.CharField(max_length=20)
   class Meta:
     db_table = "comment"
class Users(models.Model):
   name = models.CharField(max_length=5500)
   email = models.CharField(max_length=5500)
   password = models.CharField(max_length=5500)
   class Meta:
     db_table = "users"