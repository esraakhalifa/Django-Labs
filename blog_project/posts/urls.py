from django.urls import path, include
from .views import PostDetail, PostList,PostCreate, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('author/register/', RegisterView.as_view(), name='register'),
    path('author/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login, returns access & refresh tokens
    path('author/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
