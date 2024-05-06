from src.pages.page import Page

URL = "https://verified.capitalone.com/auth/signin"


class LoginPage(Page):
    def __init__(self, driver, test_parameters):
        super().__init__(driver, test_parameters)

        self.locators.update(self.all_locators["login"])

    def open(self) -> None:
        self.driver.get(URL)
        self.wait_for_element(self.locators["username"])

    def log_in(self) -> None:
        elem = self.find_element(self.locators["username"])
        self.action_chain.send_keys_to_element(
            elem, self._test_parameters["username"]
        ).perform()
        elem = self.find_element(self.locators["password"])
        self.action_chain.send_keys_to_element(
            elem, self._test_parameters["password"]
        ).perform()
        input("Click 'Sign in' button to log in, then press ENTER...")
