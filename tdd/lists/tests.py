from django.test import TestCase
from django.urls import resolve

from .models import Item
from .views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page_uses_correct_html(self):
        response = self.client.get("/")
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


class LiveTest(TestCase):
    def test_uses_list_template(self):
        response = self.client.get("/lists/only-one-list/")
        self.assertTemplateUsed(response, "list.html")

    def test_displays_all_items(self):
        item1_text = "itemy 1"
        item2_text = "itemy 2"
        Item.objects.create(text=item1_text)
        Item.objects.create(text=item2_text)

        response = self.client.get("/lists/only-one-list/")

        self.assertContains(response, item1_text)
        self.assertContains(response, item2_text)


class NewListTest(TestCase):
    def test_home_page_can_save_a_POST_request(self):
        item_text = "신규 작업 아이템"
        self.client.post("/lists/new", {"item_text": item_text})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertIn(new_item.text, item_text)

    def test_home_page_redirects_after_POST(self):
        item_text = "신규 작업 아이템"
        response = self.client.post("/lists/new", {"item_text": item_text})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["location"], "/lists/only-one-list/")
