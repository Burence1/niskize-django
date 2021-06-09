from django.db import models
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User
import uuid
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
  username = models.CharField(max_length=250, unique=True)
  email = models.EmailField(unique=True)
  first_name = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

  REQUIRED_FIELDS = []
  def __str__(self):
    return str(self.first_name)