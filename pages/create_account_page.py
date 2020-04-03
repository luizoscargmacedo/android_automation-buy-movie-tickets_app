import sys
sys.path.append("..")


from time import sleep
from .base_page import BasePage, driver


class CreateAccountPage(BasePage):
    def __init__(self):
        self.driver = driver
        self.button_next = "//android.widget.TextView[@text='Next']"
        self.input_email = "emailText"
        self.input_password = "passwordText"
        self.input_confirm_password = "confirmPasswordText"
        self.input_name = "nameText"
        self.input_nickname = "leaderboardAliasText"
        self.input_id = "externalReferenceIdText"
        self.input_x_mobile_number = "mobilex_mobileText"
        self.switch_greater_than_eighteen = "optInAgeSwitch"
        self.button_sign_up = "//android.widget.TextView"


    def input_email_send_keys(self, email):
        super().wait_visibility_of_element_located(None, self.button_next)
        self.input_email_send_keys = self.driver.find_element_by_accessibility_id(self.input_email)
        self.input_email_send_keys.send_keys(email)

    def input_password_send_keys(self, password):
        self.input_password_send_keys = self.driver.find_element_by_accessibility_id(self.input_password)
        self.input_password_send_keys.send_keys(password)

    def input_confirm_password_send_keys(self, confirm_password):
        self.input_confirm_password_send_keys = self.driver.find_element_by_accessibility_id(self.input_confirm_password)
        self.input_confirm_password_send_keys.send_keys(confirm_password)

    def button_next_tap(self):
        self.button_next_tap = self.driver.find_element_by_xpath(self.button_next)
        super().tap_element(self.button_next_tap)

    def input_name_send_keys(self, name):
        sleep(2)
        super().wait_visibility_of_element_located(None, self.button_sign_up)
        self.input_name_send_keys = self.driver.find_element_by_accessibility_id(self.input_name)
        self.input_name_send_keys.send_keys(name)

    def input_nickname_send_keys(self, nickname):
        self.input_nickname_send_keys = self.driver.find_element_by_accessibility_id(self.input_nickname)
        self.input_nickname_send_keys.send_keys(nickname)

    def input_id_send_keys(self, id):
        self.input_id_send_keys = self.driver.find_element_by_accessibility_id(self.input_id)
        self.input_id_send_keys.send_keys(id)

    def input_x_mobile_number_send_keys(self, x_mobile):
        self.input_x_mobile_number_send_keys = self.driver.find_element_by_accessibility_id(self.input_x_mobile_number)
        self.input_x_mobile_number_send_keys.send_keys(x_mobile)

    def button_sign_up_tap(self):
        self.button_sign_up_tap = self.driver.find_elements_by_xpath(self.button_sign_up)
        super().tap_element(self.button_sign_up_tap[10])

    def switch_greater_than_eighteen_tap(self, cond):
        self.switch_greater_than_eighteen_tap = self.driver.find_element_by_accessibility_id(self.switch_greater_than_eighteen)
        if cond:
            super().tap_element(self.switch_greater_than_eighteen_tap)
        else:
            pass
