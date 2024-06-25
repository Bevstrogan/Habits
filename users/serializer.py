from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "chat_id", "is_staff"]


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create(
          email=validated_data["email"],
          password=validated_data["password"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
