from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # === Locators ===
    LOGIN_BUTTON = (By.ID, 'login-btn')
    PHONE_INPUT = (By.NAME, 'phone')
    SEND_CODE_BUTTON = (By.CLASS_NAME, 'send-code')
    ICECREAM_OPTIONS = (By.CLASS_NAME, 'icecream-option')
    ORDER_BUTTON = (By.XPATH, '//button[contains(text(), "Order")]')
    CONFIRMATION_MESSAGE = (By.CSS_SELECTOR, '.confirmation')

    FROM_INPUT = (By.ID, 'route-from')
    TO_INPUT = (By.ID, 'route-to')
    SET_ROUTE_BUTTON = (By.ID, 'set-route')

    PLAN_DROPDOWN = (By.ID, 'plan-select')
    SELECTED_PLAN = (By.XPATH, '//option[@value="premium"]')

    CARD_INPUT = (By.ID, 'card-number')
    EXPIRY_INPUT = (By.ID, 'card-expiry')
    CVV_INPUT = (By.ID, 'card-cvv')
    PAY_BUTTON = (By.ID, 'pay-now')

    COMMENT_BOX = (By.ID, 'driver-comment')

    BLANKET_CHECKBOX = (By.ID, 'blanket')
    HANDKERCHIEF_CHECKBOX = (By.ID, 'handkerchief')

    CAR_SEARCH_FIELD = (By.ID, 'car-search')
    CAR_RESULT = (By.CLASS_NAME, 'car-model-result')

    # === Page Actions ===
    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def enter_phone_number(self, phone: str):
        self.wait.until(EC.presence_of_element_located(self.PHONE_INPUT)).send_keys(phone)

    def send_code(self):
        self.wait.until(EC.element_to_be_clickable(self.SEND_CODE_BUTTON)).click()

    def select_icecreams(self, count=3):
        options = self.wait.until(EC.presence_of_all_elements_located(self.ICECREAM_OPTIONS))
        for i in range(min(count, len(options))):
            options[i].click()

    def click_order(self):
        self.wait.until(EC.element_to_be_clickable(self.ORDER_BUTTON)).click()

    def get_confirmation_text(self):
        return self.wait.until(EC.presence_of_element_located(self.CONFIRMATION_MESSAGE)).text

    def set_route(self, from_location: str, to_location: str):
        self.wait.until(EC.presence_of_element_located(self.FROM_INPUT)).send_keys(from_location)
        self.wait.until(EC.presence_of_element_located(self.TO_INPUT)).send_keys(to_location)
        self.wait.until(EC.element_to_be_clickable(self.SET_ROUTE_BUTTON)).click()

    def select_plan(self):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.PLAN_DROPDOWN))
        dropdown.click()
        self.wait.until(EC.element_to_be_clickable(self.SELECTED_PLAN)).click()

    def fill_card(self, number: str, expiry: str, cvv: str):
        self.wait.until(EC.presence_of_element_located(self.CARD_INPUT)).send_keys(number)
        self.wait.until(EC.presence_of_element_located(self.EXPIRY_INPUT)).send_keys(expiry)
        self.wait.until(EC.presence_of_element_located(self.CVV_INPUT)).send_keys(cvv)
        self.wait.until(EC.element_to_be_clickable(self.PAY_BUTTON)).click()

    def comment_for_driver(self, comment: str):
        self.wait.until(EC.presence_of_element_located(self.COMMENT_BOX)).send_keys(comment)

    def order_blanket_and_handkerchiefs(self):
        self.wait.until(EC.el
