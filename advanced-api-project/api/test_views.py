from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory
from .models import Book, Author
from django.contrib.auth.models import User

class AccountTests(APITestCase):
    def test_create_book(self):
        """
        Ensure we can create a new book object.
        """
        url = reverse('add-item')
        factory = APIRequestFactory()
        snow = User(username='snowb', password='123456789')
        snowb = User(username='snow', password='12345')
        snowb.save()
        data = {'title': 'DabApps', 'author':'1', 'publication_year':'2015-03-27'}
        request = factory.get('/accounts/django-superstars/')
        self.client.force_login(snowb)
        self.client.login(snow)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'DabApps')

