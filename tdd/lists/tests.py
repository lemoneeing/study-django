from django.test import TestCase
from django.urls import resolve

from .models import Item, List
from .views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page_uses_correct_html(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")


class ListAndItemTest(TestCase):
    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        item1 = Item()
        item1.text = "첫 번째 아이템"
        item1.list = list_
        item1.save()

        item2 = Item()
        item2.text = "두 번째 아이템"
        item2.list = list_
        item2.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        self.assertEqual(saved_items[0].text, item1.text)
        self.assertEqual(item1.list, list_)
        self.assertEqual(saved_items[1].text, item2.text)
        self.assertEqual(item2.list, list_)


class LiveTest(TestCase):
    def test_uses_list_template(self):
        list_ = List.objects.create()
        response = self.client.get(f"/lists/{list_.id}/")
        self.assertTemplateUsed(response, "list.html")

    def test_displays_only_items_for_that_list(self):
        correct_list_ = List.objects.create()
        item1 = Item.objects.create(text="itemy 1", list=correct_list_)
        item2 = Item.objects.create(text="itemy 2", list=correct_list_)
        other_list_ = List.objects.create()
        other_item1 = Item.objects.create(text="other itemy 1", list=other_list_)
        other_item2 = Item.objects.create(text="other itemy 2", list=other_list_)

        response = self.client.get(f"/lists/{correct_list_.id}/")

        self.assertContains(response, item1.text)
        self.assertContains(response, item2.text)
        self.assertNotContains(response, other_item1.text)
        self.assertNotContains(response, other_item2.text)


class NewListTest(TestCase):
    def test_saving_a_POST_request(self):
        item_text = "신규 작업 아이템"
        self.client.post("/lists/new", {"item_text": item_text})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertIn(new_item.text, item_text)

    def test_redirects_after_POST(self):
        item_text = "신규 작업 아이템"
        response = self.client.post("/lists/new", data={"item_text": item_text})

        new_list = List.objects.first()
        self.assertRedirects(response, f"/lists/{new_list.id}/")


class NewItemTest(TestCase):
    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()  # noqa
        correct_list = List.objects.create()

        new_item_txt = "기존 목록에 신규 아이템"
        self.client.post(
            f"/lists/{correct_list.id}/add_item", data={"item_text": new_item_txt}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item_txt, new_item.text)
        self.assertEqual(new_item.list, correct_list)

    def test_redirects_to_list_view(self):
        correct_list = List.objects.create()
        new_item_txt = "기존 목록에 신규 아이템"
        response = self.client.post(
            f"/lists/{correct_list.id}/add_item", data={"item_text": new_item_txt}
        )

        self.assertRedirects(response, f"/lists/{correct_list.id}/")

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()  # noqa
        correct_list = List.objects.create()

        response = self.client.post(
            f"/lists/{correct_list.id}/",
        )

        self.assertEqual(response.context["list"], correct_list)
