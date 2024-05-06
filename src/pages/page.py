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
        self._timeout = self._test_parameters["default_selenium_timeout"]
        self.all_locators = get_locators()
        self.locators = {}

    def find_element(self, locator: str, root_elem: WebElement = None):
        if root_elem is None:
            return self.driver.find_element(By.XPATH, locator)
        else:
            return root_elem.find_element(By.XPATH, locator)

    def click_element(
        self, locator: str, root_elem: WebElement = None, timeout: int = 300
    ) -> None:
        elem = None
        if root_elem is not None:
            elem = self.find_element(locator, root_elem)

        start_time = datetime.now()
        while True:
            if (datetime.now() - start_time).total_seconds() > timeout:
                raise TimeoutError(
                    f"Timed out after {timeout} seconds trying to click element "
                    f"identified by locator '{locator}'."
                )
            with suppress(StaleElementReferenceException, JavascriptException):
                WebDriverWait(self.driver, self._timeout).until(
                    expected_conditions.element_to_be_clickable(
                        elem if elem is not None else (By.XPATH, locator)
                    )
                ).click()
                return

    def wait_for_element(  # TODO
        self,
        locator: str,
        root_elem: WebElement = None,
        timeout: int = None,
        extra_wait: float = None,
    ) -> WebElement:
        if timeout is None:
            timeout = self._timeout

        elem = WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located((By.XPATH, locator))
        )
        if extra_wait is not None:
            sleep(extra_wait)

        return elem

    def wait_for_element_not_visible(  # TODO
        self, locator: str, root_elem: WebElement = None
    ) -> WebElement:
        return WebDriverWait(self.driver, 600).until(
            expected_conditions.invisibility_of_element((By.XPATH, locator))
        )

    def wait_for_element_has_text(
        self, locator: str, root_elem: WebElement = None
    ) -> str:
        elem = self.find_element(locator, root_elem)

        start_time = datetime.now()
        while True:
            if (datetime.now() - start_time).total_seconds() > self._timeout:
                raise TimeoutError(
                    f"Timed out waiting for element identified by '{locator}' to have "
                    f"text."
                )
            if elem.text:
                return elem.text

    def close(self):
        self.driver.close()
