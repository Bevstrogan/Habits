from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from habits.models import Habits


class HabitsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test@example.com',
            password='123'
        )
        self.client.force_authenticate(user=self.user)

        self.habit = Habits.objects.create(
            owner=self.user,
            place='Дом',
            time="09:00:00",
            action='Готовить завтрак',
            is_pleasant_habit=False,
            related_habit=None,
            periodicity=5,
            reward='Пойти сытым на работу',
            time_to_complete=60,
            is_public=True
        )

    def test_create_habit(self):
        data = {
            "owner": self.user.id,
            "place": 'Дом',
            "time": "09:00:00",
            "action": 'Готовить завтрак',
            "is_pleasant_habit": False,
            "related_habit": "",
            "periodicity": 5,
            "reward": "Пойти сытым на работу",
            "time_to_complete": 60,
            "is_public": True
        }
        response = self.client.post(
            '/habits/create', data=data
        )
        print('RESPONSE', response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habits.objects.all().exists())

    def test_list_habit(self):
        response = self.client.get(
            '/habits/'
        )
        print('RESPONSE', response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"count": 1, "next": None, "previous": None, "results": [
            {'id': self.habit.id, 'place': 'Дом', 'time': '09:00:00', 'action': 'Готовить завтрак',
             'is_pleasant_habit': False, 'periodicity': 5, 'reward': 'Пойти сытым на работу',
             'time_to_complete': 60, 'is_public': True, 'owner': self.user.pk, 'related_habit': None}
        ]}
                         )

    def test_detail_habit(self):
        data = {
            "owner": self.user.id,
            "place": 'Дом',
            "time": "09:00:00",
            "action": 'Готовить завтрак',
            "is_pleasant_habit": False,
            "related_habit": "",
            "periodicity": 5,
            "reward": "Пойти сытым на работу",
            "time_to_complete": 60,
            "is_public": True
        }
        response = self.client.get(
            f'/habits/view/{self.habit.id}',
            data=data
        )
        print('RESPONSE', response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_habit(self):
        data = {
            "owner": self.user.id,
            "place": 'Ресторан',
            "time": "15:00:00",
            "action": 'Поесть',
            "is_pleasant_habit": True,
            "related_habit": "",
            "periodicity": 3,
            "reward": "",
            "time_to_complete": 90,
            "is_public": False
        }
        response = self.client.patch(
            f'/habits/edit/{self.habit.id}',
            data=data
        )
        print('RESPONSE', response.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.place, data["place"])
        self.assertEqual(self.habit.action, data["action"])

    def test_delete_habit(self):
        data = {
            "owner": self.user.id,
            "place": 'Ресторан',
            "time": "15:00:00",
            "action": 'Поесть',
            "is_pleasant_habit": True,
            "related_habit": "",
            "periodicity": 3,
            "reward": "",
            "time_to_complete": 90,
            "is_public": False
        }
        response = self.client.delete(
            f'/habits/delete/{self.habit.id}',
            data=data
        )
        print('RESPONSE', response.content)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)