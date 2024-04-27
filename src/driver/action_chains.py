from datetime import datetime

from selenium.common import JavascriptException
from selenium.webdriver import ActionChains as _ActionChains


class ActionChains(_ActionChains):
    def __init__(self, *args, driver, timeout, **kwargs):
        self._timeout = timeout

        super().__init__(*args, driver=driver, **kwargs)

    def perform(self) -> None:
        device_actions = [i.actions for i in self.w3c_actions.devices]

        start_time = datetime.now()
        while True:
            if (datetime.now() - start_time).total_seconds() > self._timeout:
                raise TimeoutError(
                    f"Timed out after {self._timeout} seconds trying to perform ActionChains."
                )
            try:
                super().perform()
                return
            except JavascriptException:
                # If performing the action does not succeed, reset the chained actions so they can be performed again
                for device, actions in zip(self.w3c_actions.devices, device_actions):
                    device.actions = actions
