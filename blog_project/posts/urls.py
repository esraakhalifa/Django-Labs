from django.urls import path, include
from .views import PostDetail, PostList, AuthorDetail, AuthorsList


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:post_id>/', PostDetail.as_view(), name='post_detail'),
    path('author/<int:author_id>/', AuthorDetail.as_view(), name='author_detail'),  # Updated URL pattern
    path('authors', AuthorsList.as_view(), name='author_list'),
]
