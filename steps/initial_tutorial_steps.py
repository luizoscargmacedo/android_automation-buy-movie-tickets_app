from behave import step
from time import sleep
from datetime import datetime
from hamcrest import assert_that, equal_to
import json

from pages.initial_tutorial_page import InitialTutorialPage
from pages.base_page import BasePage 

initial_tutorial_page = InitialTutorialPage()

@step(u'already screen presentation app')
def step_impl(context):
    sleep(17)
    initial_tutorial_page.button_aceitar()

@step(u'first screen validation')
def step_impl(context):
    sleep(17)
    initial_tutorial_page.button_permission()

@step(u'tap on CINEMA button in Menu')
def step_impl(context):
    initial_tutorial_page.button_cinema_tap()