from django.urls import path

from .views import HomePageView, PostDetailedView, AddPostView

app_name = 'blog'

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path('detail/<int:pk>', PostDetailedView.as_view(), name='detail'),
    path('post', AddPostView.as_view(), name='post')
]
