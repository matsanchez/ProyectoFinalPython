from django.urls import path
from .views import AboutMeView
from blog.views import ListPost

app_name="core"

urlpatterns = [
    path('', ListPost.as_view(), name='index'),
    path('about/', AboutMeView.as_view(), name="about_me")
]
