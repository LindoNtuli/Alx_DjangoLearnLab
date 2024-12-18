#accounts views
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer, LoginSerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def follow_user(self, request, pk=None):
        user_to_follow = self.get_object()
        request.user.following.add(user_to_follow)
        return Response({'status': 'following'})

    @action(detail=True, methods=['post'])
    def unfollow_user(self, request, pk=None):
        user_to_unfollow = self.get_object()
        request.user.following.remove(user_to_unfollow)
        return Response({'status': 'unfollowing'})
