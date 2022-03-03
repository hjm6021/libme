import unittest
import libme


class testSuiteTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = libme.app.test_client()

    def testRootpath(self):
        read_page = self.app.get("/")
        self.assertIn(b"Hello World!", read_page.get_data(), "예상한 응답이 아닙니다.")


if __name__ == "__main__":
    unittest.main()
