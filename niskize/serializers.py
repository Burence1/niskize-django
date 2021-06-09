from django.db import models
from django.db.models import fields
from .models import *
from django import forms
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
  class Meta:
    model=User
    fields=['id','first_name']

class ArticlesSerializers(serializers.ModelSerializer):
  class Meta:
    model = Articles
    fields='__all__'

  def to_representation(self, instance):
    rep = super().to_representation(instance)
    rep['user'] = UserSerializers(instance.user).data
    return rep

class PostsSerializers(serializers.ModelSerializer):
  class Meta:
    model = Posts
    fields='__all__'

  def to_representation(self, instance):
      rep = super().to_representation(instance)
      rep['user'] = UserSerializers(instance.user).data
      return rep

class SubscribeSerializers(serializers.ModelSerializer):
  class Meta:
    model = Subscribers
    fields='__all__'