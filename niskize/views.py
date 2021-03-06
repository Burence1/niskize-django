from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404, QueryDict
from django.http import response

# Create your views here.
class PostsLists(APIView):
  serializer_class=PostsSerializers

  def get_post(self, pk):
    try:
        return Posts.objects.get(pk=pk)
    except Posts.DoesNotExist:
        return Http404()

  def get(self, request, format=None):
    posts = Posts.objects.all()
    serializers = self.serializer_class(posts, many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers = self.serializer_class(data=request.data)
    if serializers.is_valid():
      serializers.save()
      posts = serializers.data
      response = {
          'data': {
              'posts': dict(posts),
              'status': 'success',
              'message': 'posts created successfully',
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk, format=None):
    post = self.get_post(pk)
    serializers = self.serializer_class(post, request.data)
    if serializers.is_valid():
      serializers.save()
      posts = serializers.data
      response = {
          'data': {
              'posts': dict(posts),
              'status': 'success',
              'message': ' post updated successfully',
          }
      }
      return Response(response)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    post = self.get_post(pk)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class SinglePost(APIView):
  serializer_class = PostsSerializers

  def get_post(self, pk):
    try:
        return Posts.objects.get(pk=pk)
    except Posts.DoesNotExist:
        return Http404()

  def get(self, request, pk, format=None):
    post = self.get_post(pk)
    serializers = self.serializer_class(post)
    return Response(serializers.data)

class ArticleList(APIView):
  serializer_class = ArticlesSerializers

  def get_article(self, pk):
    try:
        return Articles.objects.get(pk=pk)
    except Articles.DoesNotExist:
        return Http404()

  def get(self, request, format=None):
    articles = Articles.objects.all()
    serializers = self.serializer_class(articles, many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers = self.serializer_class(data=request.data)
    if serializers.is_valid():
      serializers.save()
      articles = serializers.data
      response = {
          'data': {
              'articles': dict(articles),
              'status': 'success',
              'message': 'article created successfully',
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk, format=None):
    article = self.get_article(pk)
    serializers = self.serializer_class(article, request.data)
    if serializers.is_valid():
      serializers.save()
      articles = serializers.data
      response = {
          'data': {
              'articles': dict(articles),
              'status': 'success',
              'message': ' article updated successfully',
          }
      }
      return Response(response)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    post = self.get_article(pk)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class SingleArticle(APIView):
  serializer_class = ArticlesSerializers

  def get_article(self, pk):
    try:
        return Articles.objects.get(pk=pk)
    except Articles.DoesNotExist:
        return Http404()

  def get(self, request, pk, format=None):
    article = self.get_article(pk)
    serializers = self.serializer_class(article)
    return Response(serializers.data)

class SubscribersList(APIView):
  serializer_class=SubscribeSerializers

  def get_subscriber(self, pk):
    try:
        return Subscribers.objects.get(pk=pk)
    except Subscribers.DoesNotExist:
        return Http404()

  def get(self, request, format=None):
    subscribers = Subscribers.objects.all()
    serializers = self.serializer_class(subscribers, many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers = self.serializer_class(data=request.data)
    if serializers.is_valid():
      serializers.save()
      subscribers = serializers.data
      response = {
          'data': {
              'subscribers': dict(subscribers),
              'status': 'success',
              'message': 'subscriber added successfully',
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    subscribers = self.get_subscriber(pk)
    subscribers.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class CommentList(APIView):
  serializer_class=CommentSerialisers

  def get_comment(self, pk):
    try:
        return Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Http404()

  def get(self, request, format=None):
    comments = Comment.objects.all()
    serializers = self.serializer_class(comments, many=True)
    return Response(serializers.data)

  def post(self, request, format=None):
    serializers = self.serializer_class(data=request.data)
    if serializers.is_valid():
      serializers.save()
      comments = serializers.data
      response = {
          'data': {
              'comments': dict(comments),
              'status': 'success',
              'message': 'comment added successfully',
          }
      }
      return Response(response, status=status.HTTP_200_OK)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk, format=None):
    comment = self.get_comment(pk)
    serializers = self.serializer_class(comment, request.data)
    if serializers.is_valid():
      serializers.save()
      comments = serializers.data
      response = {
          'data': {
              'comments': dict(comments),
              'status': 'success',
              'message': ' article updated successfully',
          }
      }
      return Response(response)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    comment = self.get_comment(pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class SingleComment(APIView):
  serializer_class = CommentSerialisers

  def get_comment(self, pk):
    try:
        return Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Http404()

  def get(self, request, pk, format=None):
    comment = self.get_comment(pk)
    serializers = self.serializer_class(comment)
    return Response(serializers.data)