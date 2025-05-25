from .models import Author, Post
from .serializers import PostSerializer, AuthorSerializer
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .permissions import IsOwner
from .tokens import CustomTokenObtainPairSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        print("INCOMING DATA:", request.data)
        serializer = self.get_serializer(data=request.data)
        try :
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("VALIDATION ERRORS:", serializer.errors)  # Log errors for debugging
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostList(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')  # Default ordering: latest first
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content', 'title', 'author__username']  # use related field
    ordering_fields = ['created_at']  # allow user-defined ordering by this field
    permission_classes = [permissions.AllowAny]

class PostCreate(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def create(self, request, *args, **kwargs):
        print("INCOMING DATA:", request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("VALIDATION ERRORS:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
               
class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]


class PostUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            if instance.image and hasattr(instance.image, 'path') and os.path.isfile(instance.image.path):
                instance.image.delete(save=False)
        except Exception as e:
            print(f"Failed to delete image file: {e}")
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
