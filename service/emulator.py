from appium import webdriver
from environment import config_capabilities, environment
import os


def capabilities(operation_system):
    desired_caps = {}
    operation_system.lower()

    desired_caps['platformName'] = config_capabilities[operation_system]["platformName"]
    desired_caps['automationName'] = config_capabilities[operation_system]["automationName"]
    desired_caps['deviceName'] = config_capabilities[operation_system]["deviceName"]
    desired_caps['appWaitActivity'] = "br.com.ingresso.ui.activities.SplashActivity"
    desired_caps['appPackage'] = "com.ingresso.cinemas"
    desired_caps["appWaitDuration"] = "20000"
    desired_caps['app'] = "{}/service/binary/{}".format(os.getcwd(), config_capabilities[environment["os"]]["app"])
   
    return desired_caps

class Emulator():
    def __init__(self):
        self.capabilities = capabilities(environment["os"])
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.capabilities)

    def set_driver(self):
        return self.driver