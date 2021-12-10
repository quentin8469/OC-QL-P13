from django.test import TestCase
from django.urls import reverse


class TestOcHomePage(TestCase):
    """"""
    
    def test_dummy(self):
        url = reverse("index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(True, b'<title>Holiday Homes</title>' in response.content)
