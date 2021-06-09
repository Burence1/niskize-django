from django.db import models
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User
import uuid
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save
from authentication.models import User
# Create your models here.

class Articles(models.Model):
  title = models.CharField(max_length=120)
  content = models.TextField()
  image=CloudinaryField('article image',null=True)
  pub_date=models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE,null=True)
  category=models.CharField(max_length=70,null=True)

  def __str__(self):
    return self.title

  class Meta:
    ordering=['-pub_date']

class Posts(models.Model):
  title=models.CharField(max_length=120,null=True)
  content=models.TextField(null=True)
  comment=models.TextField(null=True)
  pub_date=models.DateTimeField(auto_now_add=True)
  user=models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE,null=True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['-pub_date']

class Subscribers(models.Model):
  email=models.EmailField()
