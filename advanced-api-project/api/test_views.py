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
        snowb = User(username='snow', password='12345')
        snowb.save()
        data = {'title': 'DabApps', 'author':'Otimbo', 'publication_year':'2015'}
        request = factory.get('/accounts/django-superstars/')
        force_authenticate(request, user=snowb)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'DabApps')

