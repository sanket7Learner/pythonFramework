from behave import *
from commonFunctions import *

@given('I have launch {launchURL}')
def launch_URL(context,launchURL):
    fnLaunchURL(launchURL)

@when('I entered {Login_Type} as {login_Value} in {Application_Name}')
def setCredentials(context,Login_Type, login_Value , Application_Name):
    Locator_Value = fnGetLocatorValue(Application_Name,Login_Type)
    fnSetValue(Locator_Value,login_Value)

@when('I click {Element_Name} in {Application_Name}')
def clickLogin(context,Element_Name,Application_Name):
    Locator_Value = fnGetLocatorValue(Application_Name, Element_Name)
    fnClickObject(Locator_Value)

@then('I should get {login_Details} as {userToValidate:D} in {Application_Name}')
def clickLogin(context,login_Details,userToValidate,Application_Name):
    Locator_Value = fnGetLocatorValue(Application_Name, login_Details)
    fnAssertValidation(Locator_Value,userToValidate)