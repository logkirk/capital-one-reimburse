from selenium.webdriver import ChromeOptions, Chrome

options = ChromeOptions()


class ChromeDriver(Chrome):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
