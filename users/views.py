from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from users.models import User
from users.serializer import UserSerializer, CreateUserSerializer
from rest_framework.permissions import AllowAny, IsAdminUser
from users.permissions import IsOwner


class UserCreateView(CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UserRetrieveView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser, IsOwner]


class UserUpdateView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser, IsOwner]


class UserDestroyView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser, IsOwner]
