import allure


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        with allure.step("Открытие страницы"):
            self.browser.get(self.url)
