from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from habits.models import Habits
from habits.serializer import HabitsSerializer
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from users.permissions import IsOwner
from habits.pagination import HabitPagination
from habits.tasks import send_notification


class HabitCreateView(CreateAPIView):
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        send_notification(new_habit)


class HabitListView(ListAPIView):
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            queryset = Habits.objects.filter(owner=user)
        else:
            queryset = Habits.objects.all()
        return queryset


class PublicHabitListView(ListAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination


class HabitRetrieveVIew(RetrieveAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsOwner]


class HabitUpdateView(UpdateAPIView):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsOwner]


class HabitDestroyView(DestroyAPIView):
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsOwner]
