from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserListView, UserCreateView, UserRetrieveView, UserUpdateView, UserDestroyView

app_name = UsersConfig.name

urlpatterns = [
    path("", UserListView.as_view(), name="user_list"),
    path("create/", UserCreateView.as_view(), name="user_create"),
    path("view/<int:pk>", UserRetrieveView.as_view(), name="user_view"),
    path("edit/<int:pk>", UserUpdateView.as_view(), name="user_edit"),
    path("delete/<int:pk>", UserDestroyView.as_view(), name="user_delete"),
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]
