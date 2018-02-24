from behave import *

@given('I am at Login Page of CRM Portal')
def step_i_am_at_login_page_of_crm_portal(context):
    context.driver.get('http://crm.techcanvass.co.in/')

@when('I enter correct username and password and press Login for normal user')
def step_i_enter_correct_username_and_passwird_and_press_login(context):
    context.driver.find_element_by_id("btnlogin").click()
    context.driver.find_element_by_id("txtuname").send_keys("techcanvassuser@techcanvass.co.in")
    context.driver.find_element_by_id("txtpwd").send_keys("user1234")
    context.driver.find_element_by_id("loginbtn").click()

@then('I should be logged in to CRM and welcome message should be displayed')
def step_i_should_be_logged_into_crm_and_welcome_message_displayed(context):
    log_out_button_text = context.driver.find_element_by_id("ctl00_linkButton").text
    print(log_out_button_text)

@when('I enter correct username and password and press Login for admin user')
def step_i_enter_correct_username_and_password_and_press_login_admin(context):
    context.driver.find_element_by_id("btnlogin").click()
    context.driver.find_element_by_id("txtuname").send_keys("techcanvassacademy@techcanvass.co.in")
    context.driver.find_element_by_id("txtpwd").send_keys("abhishek1234")
    context.driver.find_element_by_id("loginbtn").click()

@when('I enter correct username and password and press Login for {username} and {password}')
def step_i_enter_multiple(context, username, password):
    context.driver.find_element_by_id("btnlogin").click()
    context.driver.find_element_by_id("txtuname").send_keys(username)
    context.driver.find_element_by_id("txtpwd").send_keys(password)
    context.driver.find_element_by_id("loginbtn").click()

