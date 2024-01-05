from rest_framework import generics, permissions
#from mycar_api.permissions import IsOwnerOrReadOnly
from mycar_api.permisssions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostsList(generics.ListCreateAPIView):
   
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all().order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
