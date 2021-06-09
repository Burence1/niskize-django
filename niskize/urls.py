from . import views
from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static


urlpatterns = [
    path('api/posts/',views.PostsLists.as_view()),
    #singlepost
    path('api/post/<int:pk>/',views.SinglePost.as_view()),
    #update/delete
    path('api/update/post/<int:pk>/',views.PostsLists.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)