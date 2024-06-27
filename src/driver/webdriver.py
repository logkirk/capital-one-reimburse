from undetected_chromedriver import ChromeOptions, Chrome

options = ChromeOptions()


class ChromeDriver(Chrome):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Browser version:", self.capabilities["browserVersion"])
        print(
            "Driver version:",
            self.capabilities["chrome"]["chromedriverVersion"].split(" ")[0],
        )

