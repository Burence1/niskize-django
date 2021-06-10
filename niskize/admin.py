from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Subscribers)
admin.site.register(Posts)
admin.site.register(Articles)
admin.site.register(Comment)