from . import views
from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static


urlpatterns = [
    #postsurls
    path('api/posts/',views.PostsLists.as_view()),
    #singlepost
    path('api/post/<int:pk>/',views.SinglePost.as_view()),
    #update/delete
    path('api/update/post/<int:pk>/',views.PostsLists.as_view()),

    #articlesurls
    path('api/articles/', views.ArticleList.as_view()),
    #singlepost
    path('api/article/<int:pk>/', views.SingleArticle.as_view()),
    #update/delete
    path('api/update/article/<int:pk>/', views.ArticleList.as_view()),

    #subscribers
    path('api/subscribers/', views.SubscribersList.as_view()),
    #delete
    path('api/update/subscriber/<int:pk>/', views.SubscribersList.as_view()),

    #comments
    path('api/comments/',views.CommentList.as_view()),
    #delete/update
    path('api/update/comment/<int:pk>/',views.CommentList.as_view()),
    #singlepost
    path('api/comment/<int:pk>/',views.SingleComment.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)