from django.urls import path
from .views import ListPost, CreatePost, DetailPostView, EditPostView, DeletePostView

app_name="blog"

urlpatterns = [
    path('', ListPost.as_view(), name="index"),
    path('pages/', ListPost.as_view(), name='list_post'),
    path('pages/<int:pk>/', DetailPostView.as_view(), name='detail_post'),
    path('create/', CreatePost.as_view(), name="create_post"),
    path('pages/edit/<int:pk>/', EditPostView.as_view(), name='edit_post'),
    path('pages/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
]
