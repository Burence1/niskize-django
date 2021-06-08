from django.db import models
from django.db.models import fields
from .models import *
from django import forms
from rest_framework import serializers

class ProfileSerializers(serializers.ModelSerializer):
  class Meta:
    model=Profile
    fields=['id','name']

class ArticlesSerializers(serializers.ModelSerializer):
  profile = serializers.CharField(source="profile.name")
  class Meta:
    model = Articles
    fields='__all__'

class PostsSerializers(serializers.ModelSerializer):
  profile=serializers.CharField(source="profile.name")
  class Meta:
    model = Posts
    fields='__all__'

class SubscribeSerializers(serializers.ModelSerializer):
  class Meta:
    model = Subscribers
    fields='__all__'

class UserSerializer(serializers.ModelSerializer):
  profile = serializers.CharField(source='profile.name')
  class Meta:
    model = User
    fields=['id','username','password','profile']
