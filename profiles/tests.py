from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Profile

# Create your tests here.
class TestsProfiles(TestCase):
    """"""
    def setUp(self):
        user = User.objects.create(username='testuser', password='u1234')
        print(str(user))
        profile = Profile.objects.create(user=user , favorite_city='testLyon')
        print(profile)
    
    def test_profiles_index(self):
        url = reverse('profiles:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<title>Profiles</title>", response.content)
    
    def test_profiles_profile(self):
        url = reverse('profiles:profile', args=['testuser'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<title>testuser</title>", response.content)
        