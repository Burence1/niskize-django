from django.db import models
from django.db.models import fields
from .models import *
from django import forms
from rest_framework import serializers

class ProfileSerializers(serializers.ModelSerializer):
  # name = serializers.SerializerMethodField()
  class Meta:
    model=Profile
    fields=['id','name']

  # def get_name(self, profile):
  #     return profile.name

  # def to_representation(self, instance):
  #     rep = super().to_representation(instance)
  #     rep['name'] = ProfileSerializers(instance.name).data
  #     return rep

class ArticlesSerializers(serializers.ModelSerializer):
  profile = serializers.CharField(source="profile.name")
  class Meta:
    model = Articles
    fields='__all__'

class PostsSerializers(serializers.ModelSerializer):
  class Meta:
    model = Posts
    fields='__all__'

  def to_representation(self, instance):
      rep = super().to_representation(instance)
      rep['profile'] = ProfileSerializers(instance.profile).data
      return rep

class SubscribeSerializers(serializers.ModelSerializer):
  class Meta:
    model = Subscribers
    fields='__all__'

class UserSerializer(serializers.ModelSerializer):
  profile = serializers.CharField(source='profile.name')
  class Meta:
    model = User
    fields=['id','username','password','profile']
