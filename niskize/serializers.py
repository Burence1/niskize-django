from django.db import models
from django.db.models import fields
from .models import *
from django import forms
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
  username = serializers.SerializerMethodField()
  class Meta:
    model=User
    fields=['id','first_name']

  @classmethod
  def get_username(self, cls):
      return cls.username


class ArticlesSerializers(serializers.ModelSerializer):
  username = serializers.SerializerMethodField()
  class Meta:
    model = Articles
    fields='__all__'

  @classmethod
  def get_username(self, cls):
      return cls.user.username

class PostsSerializers(serializers.ModelSerializer):
  first_name = serializers.SerializerMethodField()
  class Meta:
    model = Posts
    fields='__all__'
    

  @classmethod
  def get_first_name(self, cls):
      return cls.user.first_name

  
class SubscribeSerializers(serializers.ModelSerializer):
  class Meta:
    model = Subscribers
    fields='__all__'

class CommentSerialisers(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields='__all__'
    
