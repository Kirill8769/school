from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lesson.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='testuser1@mail.com')
        self.lesson = Lesson.objects.create(title='title', description='description', owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_list(self):
        """Тестирование вывода списка уроков"""

        url = reverse('lessons:lesson_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_create(self):
        """Тестирование создания урока"""

        url = reverse('lessons:lesson_create')
        data = {
            'title': 'title2',
            'description': 'description2'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        """Тестирование обновления урока"""

        url = reverse('lesson:lesson_update', args=(self.lesson.pk, ))
        update_data = {
            'title': 'title_update'
        }
        response = self.client.patch(url, update_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), update_data.get('title'))

    def test_lesson_retrieve(self):
        """Тестирование детального просмотра урока"""

        url = reverse('lesson:lesson_detail', args=(self.lesson.pk, ))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), self.lesson.title)

    def test_lesson_delete(self):
        """Тестирование удаления урока"""

        url = reverse('lesson:lesson_delete', args=(self.lesson.pk, ))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)
