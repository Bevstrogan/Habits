from django.db import models

from users.models import User


class Habits(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель привычки")
    place = models.CharField(max_length=200, verbose_name="Место для привычки")
    time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Время для привычки")
    action = models.CharField(max_length=300, verbose_name="Привычка")
    is_pleasant_habit = models.BooleanField(default=True, verbose_name="Признак приятной привычки", null=True, blank=True)
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Связанная привычка")
    periodicity = models.IntegerField(default=1, verbose_name="Периодичность привычки в неделю")
    reward = models.CharField(max_length=100, null=True, blank=True, verbose_name="Вознаграждение")
    time_to_complete = models.IntegerField(verbose_name="Время на выполнение")
    is_public = models.BooleanField(default=True, verbose_name="Признак публичности")

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"