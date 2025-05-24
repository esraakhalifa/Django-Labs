from .models import Author, Post
from .serializers import PostSerializer, AuthorSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        print("INCOMING DATA:", request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Assign author on the server side (hardcoded here for example)
            serializer.save(author=Author.objects.first())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("VALIDATION ERRORS:", serializer.errors)  # Log errors for debugging
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            if instance.image and hasattr(instance.image, 'path') and os.path.isfile(instance.image.path):
                instance.image.delete(save=False)
        except Exception as e:
            print(f"Failed to delete image file: {e}")
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
