import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def check_for_rows_in_list_table(self, row_txt):
        # 다시 페이지가 갱신되고 화면에 두 개의 아이템이 표시된다.
        table = self.browser.find_element(by=By.ID, value="id_list_table")
        rows = table.find_elements(by=By.TAG_NAME, value="tr")
        self.assertIn(row_txt, [row.text for row in rows])

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve_it_later(self):
        # 사용자는 새로나온 작업목록 관리 사이트에 방문한다.
        self.browser.get("http://localhost:8080")

        # 웹 페이지 타이틀과 헤더에 'To-Do' 라고 표시된다.
        self.assertIn("To-Do", self.browser.title)
        header = self.browser.find_element(by=By.TAG_NAME, value="h1")
        self.assertIn("To-Do", header.text)

        # 사용자는 작업 목록을 추가한다.
        input_box = self.browser.find_element(by=By.ID, value="id_new_item")
        self.assertEqual(input_box.get_attribute("placeholder"), "작업 아이템 입력")

        # 텍스트상자에 '공작 깃털 사기'를 입력한다.
        item1 = "공작 깃털 사기"
        input_box.send_keys(item1)

        # Enter 키를 누르면 페이지가 갱신되고
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # 작업목록에 '1: 공작 깃털 사기' 아이템이 추가된다.
        self.check_for_rows_in_list_table(f"1: {item1}")

        # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 있다.
        # 사용자는 한 번 더 아이템을 입력한다: '공작 깃털로 그물만들기'
        item2 = "공작 깃털로 그물만들기"
        input_box = self.browser.find_element(by=By.ID, value="id_new_item")
        input_box.send_keys(item2)

        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        # 다시 페이지가 갱신되고 화면에 두 개의 아이템이 표시된다.
        self.check_for_rows_in_list_table(f"1: {item1}")
        self.check_for_rows_in_list_table(f"2: {item2}")

        # 사용자는 추가한 작업 목록이 웹 서버에 저장되어 있는지 확인하고 싶다.
        # 사이트는 사용자를 위한 특정 URL 을 제공한다.
        # URL에 대한 설명도 함께 제공한다.
        self.fail("Finish the test!")

        # 해당 URL 에 접속하면 사용자가 만든 작업 목록을 확인할 수 있다.


if __name__ == "__main__":
    unittest.main(warnings="ignore")
