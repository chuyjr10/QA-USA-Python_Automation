from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options
        options = webdriver.ChromeOptions()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(options=options)
        cls.page = UrbanRoutesPage(cls.driver)
        cls.driver.get("https://cnt-1536bf49-03a6-471e-b060-2c1c10ac7bc2.containerhub.tripleten-services.com/")  # ⛔ Replace with real URL

    def test_user_can_login_and_order_icecream(self):
        self.page.click_login_button()
        self.page.enter_phone_number("1234567890")
        self.page.send_code()
        self.page.select_icecreams(count=3)
        self.page.click_order()
        confirmation = self.page.get_confirmation_text()
        assert "Thank you" in confirmation or "confirmed" in confirmation.lower()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
