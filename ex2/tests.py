from django.test import TestCase
from django.contrib.auth.models import User
from .utils import bubble_sort


class FunctionalTests(TestCase):

    def setUp(self):
        User.objects.create_superuser('admin', '', 'admin')
        self.client.login(username='admin', password='admin')

    def test_sort_view(self):
        response = self.client.post('/ex2/sort/',
                                    {'input': ' -5, 4.2,3,2.0,1  '}
                                    )
        self.assertEquals(response.content,
                          '{"result": [-5, 1, 2.0, 3, 4.2]}')


class BubbleSortTests(TestCase):

    def test_integer_sorting(self):
        self.assertEquals(
            bubble_sort([1, 5, 8, 4, 2, 6, 7]),
            [1, 2, 4, 5, 6, 7, 8])

    def test_fraction_sorting(self):
        self.assertEquals(
            bubble_sort([3.4, 10.2, 5.0, -5.1222]),
            [-5.1222, 3.4, 5.0, 10.2]
        )
