from behave import *
from commonFunctions import *

@given('I have launch {launchURL}')
def launch_URL(context,launchURL):
    fnLaunchURL(launchURL)

@when('I enter username {userName:D} and password {password}')
def setCredentials(context,userName,password):
    fnSetValue("hrm_username",userName)
    fnSetValue("hrm_password",password )

@when('I click {loginButton}')
def clickLogin(context,loginButton):
    fnClickObject("hrm_loginbutton")

@then('I should get user as {userToValidate:D}')
def clickLogin(context,userToValidate):
    fnAssertValidation("hrm_loginid",userToValidate)