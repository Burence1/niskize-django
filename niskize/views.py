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
    post = self.get_post(pk)
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