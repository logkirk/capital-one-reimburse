from contextlib import suppress
from datetime import datetime
from time import sleep

from selenium.common import StaleElementReferenceException, JavascriptException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.driver.action_chains import ActionChains
from src.locators.locators import get_locators


class Page:
    def __init__(self, driver, test_parameters):
        self.driver = driver
        self.action_chain = ActionChains(
            driver=self.driver, timeout=test_parameters["actionchains_timeout"]
        )
        self._test_parameters = test_parameters
        self.all_locators = get_locators()
        self.locators = {}

    def find_element(self, locator: str):
        return self.driver.find_element(By.XPATH, locator)

    def click_element(self, locator: str, timeout: int = 300) -> None:
        start_time = datetime.now()
        while True:
            if (datetime.now() - start_time).total_seconds() > timeout:
                raise TimeoutError(
                    f"Timed out after {timeout} seconds trying to click element "
                    f"identified by locator '{locator}'."
                )
            with suppress(StaleElementReferenceException, JavascriptException):
                WebDriverWait(
                    self.driver, self._test_parameters["default_selenium_timeout"]
                ).until(
                    expected_conditions.element_to_be_clickable((By.XPATH, locator))
                ).click()
                return

    def wait_for_element(self, locator: str, extra_wait: float = None) -> WebElement:
        elem = WebDriverWait(
            self.driver, self._test_parameters["default_selenium_timeout"]
        ).until(expected_conditions.presence_of_element_located((By.XPATH, locator)))
        if extra_wait is not None:
            sleep(extra_wait)

        return elem

    def wait_for_element_not_visible(self, locator: str) -> WebElement:
        return WebDriverWait(self.driver, 600).until(
            expected_conditions.invisibility_of_element((By.XPATH, locator))
        )

    def close(self):
        self.driver.close()
