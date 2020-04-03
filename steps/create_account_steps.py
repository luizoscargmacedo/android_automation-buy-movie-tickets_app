from behave import step

from pages.create_account_page import CreateAccountPage
from pages.base_page import BasePage
from helpers.helpers import faker

create_account_page = CreateAccountPage()


@step(u'fill all information')
def step_impl(context):
    context.email = faker.email()

    for keys in context.table:
        create_account_page.input_email_send_keys(context.email)
        create_account_page.input_password_send_keys(keys["password"])
        create_account_page.input_confirm_password_send_keys(keys["confirm_password"])
        
    BasePage().allure_take_screenshot("Personal_information_first")


@step(u'tap in button NEXT')
def step_impl(context):
    create_account_page.button_next_tap()

@step(u'fill the personal information fields')
def step_impl(context):
    context.name = faker.name()
    context.nickname =  f"{faker.suffix_male()}_{faker.safe_color_name()}"
    context.id = gen.id()
    context.x_mobile_number = faker.msisdn()

    create_account_page.input_name_send_keys(context.name)
    create_account_page.input_nickname_send_keys(context.nickname)
    create_account_page.input_id_send_keys(context.id)
    create_account_page.input_x_mobile_number_send_keys(context.x_mobile_number)
    for keys in context.table:
        create_account_page.switch_greater_than_eighteen_tap(keys["switch_greater_than_eighteen"])
    BasePage().allure_take_screenshot("Personal_information_second")

@step(u'verify if all information are correct')
def step_impl(context):
    BasePage().allure_take_screenshot("Personal_information_correct")

@step('button REGISTER must be enabled and tap it')
def step_impl(context):
    create_account_page.button_sign_up_tap()
