from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import BlogPost
from .serializers import BlogPostSerializers


# Create your views here.
class BlogPostListCreate(ListCreateAPIView):
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializers

  def delete(self, request, *args, **kwargs):
    BlogPost.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  
class BlogPostRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializers
  lookup_field = "pk"

