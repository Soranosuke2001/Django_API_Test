from django.urls import path

from .views import BlogPostListCreate, BlogPostRetrieveUpdateDestroy

app_name = 'api'

urlpatterns = [
  path("blogposts/", BlogPostListCreate.as_view(), name="blogpost-view-create"),
  path("blogposts/<int:pk>/", BlogPostRetrieveUpdateDestroy.as_view(), name="update"),
]
