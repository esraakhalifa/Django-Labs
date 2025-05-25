from django.urls import path, include
from .views import PostRetrieveView, PostUpdateDeleteView, PostList,PostCreate, RegisterView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import  TokenRefreshView


urlpatterns = [ 
    path('', PostList.as_view(), name='post_list'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/', PostRetrieveView.as_view(), name='post-detail'),
    path('<int:pk>/edit/', PostUpdateDeleteView.as_view(), name='post-update-delete'),
    path('author/register/', RegisterView.as_view(), name='register'),
    path('author/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # login, returns access & refresh tokens
    path('author/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
