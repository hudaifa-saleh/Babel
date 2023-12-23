from django.test import TestCase
from django.urls import reverse


class HomePageViewTest(TestCase):
    def test_home_page_view_template(self):
        response = self.client.get(reverse("home"))  # Assuming 'home' is the URL name for HomePageView

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "templates/home.html")
