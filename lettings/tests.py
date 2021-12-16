from django.test import TestCase
from django.urls import reverse

from lettings.models import Letting, Address

# Create your tests here.


class TestsLettings(TestCase):
    """"""
    
    def setUp(self):
        address = Address.objects.create(number=1, street='street', city='Top City', 
                                         state='state', zip_code=1234, country_iso_code='fr')
        letting = Letting.objects.create(title='Au top', address=address)
    
    def test_lettings_index(self):
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<title>Lettings</title>", response.content)
    
    def test_lettings_letting(self):
        url = reverse('lettings:letting', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<title>Au top</title>", response.content)