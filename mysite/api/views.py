from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView

from .models import BlogPost
from .serializers import BlogPostSerializers


# Create your views here.
class BlogPostListCreate(ListCreateAPIView):
  queryset = BlogPost.objects.all()
  serializer_class = BlogPostSerializers

  