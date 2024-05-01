from unittest import TestCase
from yaml import safe_load

from src.pages.example import ExamplePage
from src.driver.webdriver import ChromeDriver


class ExampleTestSuite(TestCase):
    parameters = None

    @classmethod
    def setUpClass(cls):
        with open("parameters.yaml", "r") as f:
            cls.parameters = safe_load(f)

    def setUp(self):
        self.driver = ChromeDriver()

    def test_example(self):
        example_page = ExamplePage(driver=self.driver, test_parameters=self.parameters)
        example_page.driver.get("https://www.example.com")
        elem = example_page.find_element(example_page.locators["example_header"])
        self.assertEqual(elem.text, "Example Domain")
