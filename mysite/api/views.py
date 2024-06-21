from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

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


class BlogPostList(APIView):
  def get(self, request, format=None):
    title = request.query_params.get("title", "")

    if title:
      blog_posts = BlogPost.objects.filter(title__icontains=title)
    else:
      blog_posts = BlogPost.objects.all()

    serializer = BlogPostSerializers(blog_posts, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request, format=None):
    serializer = BlogPostSerializers(data=request.data)

    if serializer.is_valid():
      # Saves to Database
      serializer.save()

      return Response(status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

  