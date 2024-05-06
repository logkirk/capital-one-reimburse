from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.pages.page import Page

URL = r""  # Temp removed for security


class PurchasesPage(Page):
    def __init__(self, driver, test_parameters):
        super().__init__(driver, test_parameters)

        self.locators.update(self.all_locators["purchases"])

    def open(self) -> None:
        self.driver.get(URL)
        self.wait_for_element(self.locators["purchase_cards"])

    def get_first_purchase_card(self) -> [WebElement]:
        return self.wait_for_element(self.locators["purchase_cards"], timeout=10)

    def get_purchase_date(self, element):
        return self.wait_for_element_has_text(
            locator=self.locators["date"], root_elem=element
        ).strip()

    def get_purchase_merchant(self, element):
        return self.wait_for_element_has_text(
            locator=self.locators["merchant"], root_elem=element
        ).strip()

    def get_purchase_cost(self, element):
        return self.wait_for_element_has_text(
            locator=self.locators["cost"], root_elem=element
        ).strip()

    def reimburse(self, element) -> (str, str, str):
        element.find_element(By.XPATH, self.locators["radio_button"])
        self.find_element(self.locators["continue_button"]).click()
        self.wait_for_element(self.locators["confirm_button"])
        miles_elems = self.driver.find_elements(By.XPATH, self.locators["miles_fields"])
        miles_available = miles_elems[0].text
        miles_redeemed = miles_elems[1].text
        remaining_miles = miles_elems[2].text
        self.click_element(self.locators["confirm_button"])
        self.wait_for_element(self.locators["success"])
        confirmation = self.find_element(self.locators["confirmation"]).text
        return miles_available, miles_redeemed, remaining_miles, confirmation
