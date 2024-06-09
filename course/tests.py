from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='testuser1@mail.com')
        self.course = Course.objects.create(title='title', description='description', owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_course_list(self):
        """Тестирование вывода списка курсов"""

        url = reverse('courses:course-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_create(self):
        """Тестирование создания курса"""

        url = reverse('courses:course-list')
        data = {
            'title': 'title2',
            'description': 'description2'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.all().count(), 2)

    def test_course_update(self):
        """Тестирование обновления курса"""

        url = reverse('courses:course-detail', args=(self.course.pk, ))
        update_data = {
            'title': 'title_update'
        }
        response = self.client.patch(url, update_data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), update_data.get('title'))

    def test_course_retrieve(self):
        """Тестирование детального просмотра курса"""

        url = reverse('courses:course-detail', args=(self.course.pk, ))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('title'), self.course.title)

    def test_course_delete(self):
        """Тестирование удаления курса"""

        url = reverse('courses:course-detail', args=(self.course.pk, ))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.all().count(), 0)
