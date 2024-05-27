from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
  path("list/", PostListView.as_view(), name="list"),
  path("detail/", PostDetailView.as_view(), name="detail"),
  path("new/", PostCreateView.as_view(), name="new"),
]