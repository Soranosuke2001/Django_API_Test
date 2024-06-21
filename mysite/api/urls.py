from django.urls import path

from .views import BlogPostListCreate

app_name = 'api'

urlpatterns = [
  path("blogposts/", BlogPostListCreate.as_view(), name="blogpost-view-create"),
]
