# Generated by Django 5.0.6 on 2024-06-25 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habits",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place",
                    models.CharField(max_length=200, verbose_name="Место для привычки"),
                ),
                ("time", models.TimeField(verbose_name="Время для привычки")),
                ("action", models.CharField(max_length=300, verbose_name="Привычка")),
                (
                    "is_pleasant_habit",
                    models.BooleanField(
                        blank=True,
                        default=True,
                        null=True,
                        verbose_name="Признак приятной привычки",
                    ),
                ),
                (
                    "periodicity",
                    models.IntegerField(
                        default=1, verbose_name="Периодичность привычки в неделю"
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "time_to_complete",
                    models.IntegerField(verbose_name="Время на выполнение"),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=True, verbose_name="Признак публичности"
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]
