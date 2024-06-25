from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("habits.urls"), name="habits"),
    path("users/", include("users.urls"), name="users"),
]
