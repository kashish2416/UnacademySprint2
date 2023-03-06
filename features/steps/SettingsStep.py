
import time
from behave import *
from hamcrest import *


from features.pages.LandingPageClass import LandingPageClass

from features.pages.HomePageClass import HomePageClass
from features.pages.SettingsPageClass import SettingsPageClass

#Scenario1
@given("Chrome is opened and Unacademy app is opened")
def step_impl(context):
   pass


@when("User clicks on login button")
def step_impl(context):

   lp = LandingPageClass(context.driver)
   lp.click_login_button()
   context.driver.implicitly_wait(20)


@when(u'User enters Mobile Number "{mn}"')
def step_impl(context,mn):
    time.sleep(20)
    mTextBox=LandingPageClass(context.driver)
    mTextBox.enter_mobilenumber_textbox(mn)


@step("User again clicks on login button")
def step_impl(context):
    time.sleep(2)
    SB=LandingPageClass(context.driver)
    SB.click_secondlogin_button()


@step(u'User enters otp')
def step_impl(context):

   time.sleep(20)


@step("User clicks on verify otp button")
def step_impl(context):

    time.sleep(10)
    votp=LandingPageClass(context.driver)
    votp.click_verifyOtp_button()


@step("User clicks on Profile button")
def step_impl(context):
    time.sleep(20)
    pfb=HomePageClass(context.driver)
    pfb.click_profile_button()

@step("User clicks on settings")
def step_impl(context):
    time.sleep(20)
    sb=HomePageClass(context.driver)
    sb.click_settings_button()


@then("It shows settings page")
def step_impl(context):
    time.sleep(5)
    expectedTitle = "Unacademy - India's largest learning platform"
    actualTitle = context.driver.title
    print(actualTitle)
    assert_that(expectedTitle,equal_to(actualTitle))

#Scenario2
@step("User clicks on edit state button")
def step_impl(context):
    time.sleep(5)
    eb=SettingsPageClass(context.driver)
    eb.click_editstate_buttonelement()


@step("Clicks on save button")
def step_impl(context):

    time.sleep(2)
    sb=SettingsPageClass(context.driver)
    sb.click_save_button()

@then("It shows updated state")
def step_impl(context):
    pass


#Scenario3
@step("User clicks on email field")
def step_impl(context):

    time.sleep(3)
    sf=SettingsPageClass(context.driver)
    sf.click_editEmail_button()
    #context.driver.implicitly_wait(20)


@step("User clicks on refresh button")
def step_impl(context):

    time.sleep(2)
    refresh=SettingsPageClass(context.driver)
    refresh.refresh_button()

@then("The page gets refreshed and user remains on same page")
def step_impl(context):

    time.sleep(3)
    '''
    expectedTitle = "Unacademy - India's largest learning platform"
    actualTitle = context.driver.title
    print(actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
    '''
    expectedURL = "https://unacademy.com/settings"
    pageURL = context.driver.current_url
    print(pageURL)
    assert_that(expectedURL, equal_to(pageURL))


#Scenario 4&5


@step("User click on username field")
def step_impl(context):

    time.sleep(5)
    clickuname=SettingsPageClass(context.driver)
    clickuname.click_edit_username_button()


@step(u'User enters "{uname}"')
def step_impl(context, uname):

    time.sleep(10)
    enteruname=SettingsPageClass(context.driver)
    enteruname.enter_username_textbox(uname)




@step(u'User enters {invuname}')
def step_impl(context, invuname):

    time.sleep(10)
    enteruname = SettingsPageClass(context.driver)
    enteruname.enter_invusername_textbox(invuname)


@then("It shows updated username")
def step_impl(context):
    pass

@then("username is not updated")
def step_impl(context):
    pass


