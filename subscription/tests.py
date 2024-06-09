from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course
from subscription.models import Subscription
from users.models import User


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='testuser1@mail.com')
        self.course = Course.objects.create(title='title', description='description', owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_change_subscription(self):
        """Тестирование активации/деактивации подписки"""

        url = reverse('subscriptions:subscription')
        course_url = reverse('courses:course-detail', args=(self.course.pk, ))
        data = {
            'user': self.user,
            'course': self.course.pk
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())
        course_response = self.client.get(course_url)
        course_data = course_response.json()
        self.assertEqual(course_response.status_code, status.HTTP_200_OK)
        self.assertTrue(course_data['is_subscribe'])

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())
        course_response = self.client.get(course_url)
        course_data = course_response.json()
        self.assertEqual(course_response.status_code, status.HTTP_200_OK)
        self.assertFalse(course_data['is_subscribe'])
