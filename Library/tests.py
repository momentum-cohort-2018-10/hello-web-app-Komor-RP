from django.test import TestCase


# Create your tests here.
class CollectionTest(TestCase):
    def test_index(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)

    def test_about_page(self):
        r = self.client.get('/about/')
        self.assertEqual(r.status_code, 200)

    def test_contact_page(self):
        r = self.client.get('/contact/')
        self.assertEqual(r.status_code, 200)
