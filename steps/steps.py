from behave import step
from time import sleep

@step(u'wait {seconds} seconds')
def step_impl(context, seconds):
    sleep(int(seconds))