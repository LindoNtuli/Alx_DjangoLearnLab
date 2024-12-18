#posts views
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from rest_framework.views import APIView
from rest_framework.response import Response
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
