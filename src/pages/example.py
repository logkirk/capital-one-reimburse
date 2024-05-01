from src.pages.page import Page


class ExamplePage(Page):
    def __init__(self, driver, test_parameters):
        super().__init__(driver, test_parameters)

        self.locators.update(self.all_locators["example"])
