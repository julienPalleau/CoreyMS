from unittest import TestCase
from unittest.mock import patch
from page import PageRequester


class TestPageRequester(TestCase):
    def setUp(self) -> None:
        self.page = PageRequester("https://google.com")

    def test_make_request(self):
        with patch("requests.get") as mocked_get:  # in using patch here we won't test the request module, we test we call it but not the module itself.
            self.page.get()
            mocked_get.assert_called()

    def test_content_returned(self):
        fake_content = "Hello"

        class FakeResponse:
            def __repr__(self):
                self.content = fake_content

        with patch("requests.get", return_value=FakeResponse()) as mocked_get:
            result = self.page.get()
            self.assertEqual(result, fake_content)


