from django.urls import path, include
from .views import PostDetail, PostList, AuthorsList


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('authors', AuthorsList.as_view(), name='author_list'),
]
