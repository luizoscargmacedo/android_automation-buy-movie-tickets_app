import allure 
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from datetime import datetime
from time import sleep

from service.emulator import Emulator
from helpers.constants import TIMEOUT
from helpers.constants import FOLDER_SCREENSHOT

driver = Emulator().set_driver()
wait = WebDriverWait(driver, TIMEOUT)
action = TouchAction(driver)


class BasePage():
    def __init__(self):
        self.driver = driver

    def wait_element_to_be_clickable(self, type, element):
        if type is None:
            return wait.until(EC.element_to_be_clickable((By.XPATH, element)))
        else:
            return wait.until(EC.element_to_be_clickable((By.ID, element)))

    def wait_visibility_of_element_located(self,type, element):
        if type is None:
            return wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        else:
            return wait.until(EC.visibility_of_element_located((By.ID, element)))

    def wait_presence_of_all_elements_located(self, type, element):
        if type is None:
            return wait.until(EC.presence_of_all_elements_located((By.XPATH, element)))
        else:
            return wait.until(EC.presence_of_all_elements_located((By.ID, element)))

    def wait_invisibility_of_element_located(self, type, element):
        if type is None:
            return wait.until(EC.invisibility_of_element_located((By.XPATH, element)))
        else:
            return wait.until(EC.invisibility_of_element_located((By.ID, element)))

    def tap_element(self, element):
        action.tap(element).perform()

    def long_click_element(self, element):
        action.long_press(element).perform()

    def double_click_element(self, element):
        action.tap(element, count=2).perform()

    def lazy_double_click_tap(self, element):
        for x in range(0,2):
            action.press(element).wait(1500).perform()

    def fill_field(self, element,value):
        element.send_keys(value)

    def allure_take_screenshot(self, namefile):
        allure.attach(self.driver.get_screenshot_as_png(),
        name=f"{datetime.now()}-{namefile}", attachment_type=AttachmentType.PNG)

    def take_screenshot(self, namefile):
        self.driver.save_screenshot(f"{FOLDER_SCREENSHOT}/{namefile}.png")

    def swipe_screen_left(self, lista=[]):
        self.driver.swipe(list[0], list[1], list[2], list[3])

    def drag_and_drop_element(self, firt_element, second_element):
        self.driver.drag_and_drop(firt_element, second_element)

    def verify_text_in_activity(self, message):
        return message in self.driver.page_source

    def get_current_activity(self):
        return self.driver.current_activity

    def tap_x_y(self, x=100, y=100):
        action.tap(None, x, y, 1).perform()