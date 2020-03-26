import sys
sys.path.append("..")

from datetime import datetime
from hamcrest import assert_that, equal_to

from pages.base_page import BasePage, driver
from service.emulator import config_capabilities, environment
from time import sleep

from appium import webdriver

from random import randint
from selenium.webdriver.common.keys import keys

class InitialTutorialPage(BasePage):
    def __init__(self):
        self.driver = driver
        self.button_agree_terms = "//android.widget.TextView[@text='ACEITAR']"
        self.button_agree_permission = "//android.widget.TextView[@text='Allow all the time']"
        self.button_cinema = "//android.widget.id[com.ingresso.cinemas:id/tab_theater]"

    def button_aceitar(self):
        sleep(17)
        button_agree_terms_tap = self.driver.find_element_by_xpath(self.button_agree_terms)
        super().tap_element(button_agree_terms_tap)

    def button_permission(self):
        sleep(3)
        button_agree_permission_tap = self.driver.find_element_by_xpath(self.button_agree_permission)
        super().tap_element(button_agree_permission_tap)

    def button_cinema_tap(self):
        sleep(3)
        self.button_login_tap = driver.find_element_by_xpath(self.button_cinema)
        super().tap_element(self.button_cinema_tap)