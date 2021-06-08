from django.db import models
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
  name = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

  def __str__(self):
    return self.user.username
  
  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
      if created:
          Profile.objects.create(user=instance)
  
  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()

class Articles(models.Model):
  title = models.CharField(max_length=120)
  content = models.TextField()
  pub_date=models.DateTimeField(auto_now_add=True)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
  category=models.CharField(max_length=70,null=True)

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
