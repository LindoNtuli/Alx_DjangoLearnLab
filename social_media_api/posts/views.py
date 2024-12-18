#posts views
from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like, Notification
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import PostSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['title', 'content']
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        # Create a Like entry
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        # Create a notification
        if created:  # If the like was created (not an existing like)
            Notification.objects.create(user=post.author, message=f"{request.user.username} liked your post.")

        return Response({'status': 'liked', 'post_id': pk})

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        # Remove the Like entry if it exists
        Like.objects.filter(user=request.user, post=post).delete()
        
        # Create a notification for unliking if necessary
        Notification.objects.create(user=post.author, message=f"{request.user.username} unliked your post.")
        
        return Response({'status': 'unliked', 'post_id': pk})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get the users the current user is following
        following_users = request.user.following.all()
        # Retrieve posts from those users, ordered by creation date
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
