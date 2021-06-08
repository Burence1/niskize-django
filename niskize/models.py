from django.db import models
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.user.username


class Articles(models.Model):
  title = models.CharField(max_length=120)
  content = models.TextField()
  pub_date=models.DateTimeField(auto_now_add=True)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)

  def __str__(self):
    return self.title

  class Meta:
    ordering=['-pub_date']

class Posts(models.Model):
  title=models.CharField(max_length=120,null=True)
  content=models.TextField()
  comment=models.TextField()
  pub_date=models.DateTimeField(auto_now_add=True)
  profile=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['-pub_date']

class Subscribers(models.Model):
  email=models.EmailField()
