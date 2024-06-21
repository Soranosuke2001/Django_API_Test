from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import BlogPost
from .serializers import BlogPostSerializers


# Create your views here.
class BlogPostListCreate(ListCreateAPIView):
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializers

  
class BlogPostRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializers
  lookup_field = "pk"

  