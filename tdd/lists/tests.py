from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from .models import Item
from .views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # request = HttpRequest()
        # response = home_page(request)
        # expected_html = render_to_string("home.html")
        # self.assertEqual(response.content.decode(), expected_html)
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = "POST"
        item_text = "신규 작업 아이템"
        request.POST["item_text"] = item_text

        # response = home_page(request)
        response = self.client.post("/", request.POST)

        self.assertIn(item_text, response.content.decode())
        # expected_html = render_to_string("home.html", {"new_item_text": item_text})
        # self.assertEqual(response.content.decode(), expected_html)
        self.assertTemplateUsed(response, "home.html")


class ItemTest(TestCase):
    def test_saving_and_retrieving_items(self):
        item1 = Item()
        item1.text = "첫 번째 아이템"
        item1.save()

        item2 = Item()
        item2.text = "두 번째 아이템"
        item2.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        self.assertEqual(saved_items[0].text, item1.text)
        self.assertEqual(saved_items[1].text, item2.text)
