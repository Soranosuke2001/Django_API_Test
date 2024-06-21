from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
  path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
  path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name="update"),
  path("blogposts/search/", views.BlogPostList.as_view(), name="search"),
]
