import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve_it_later(self):
        # 사용자는 새로나온 작업목록 관리 사이트에 방문한다.
        self.browser.get("http://localhost:8080")
        self.browser.implicitly_wait(3)

        # 웹 페이지 타이틀과 헤더에 'To-Do' 라고 표시된다.
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")

        # 사용자는 작업 목록을 추가한다.
        # 텍스트상자에 '공작 깃털 사기'를 입력한다.

        # Enter 키를 누르면 페이지가 갱신되고
        # 작업목록에 '1. 공작 깃털 사기' 아이템이 추가된다.

        # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 있다.

        # 사용자는 한 번 더 아이템을 입력한다: '공작 깃털로 그물만들기'

        # 다시 페이지가 갱신되고 화면에 두 개의 아이템이 표시된다.

        # 사용자는 추가한 작업 목록이 웹 서버에 저장되어 있는지 확인하고 싶다.
        # 사이트는 사용자를 위한 특정 URL 을 제공한다.
        # URL에 대한 설명도 함께 제공한다.

        # 해당 URL 에 접속하면 사용자가 만든 작업 목록을 확인할 수 있다.


if __name__ == "__main__":
    unittest.main(warnings="ignore")
