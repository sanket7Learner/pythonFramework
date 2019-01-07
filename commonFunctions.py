from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from globalLocators import oGlobalLocatorDict
from Utils import *
import os
import time

driver = None
wait = None

def fnLaunchURL(urlName):

   global driver

   if driver :
       driver.close()
       driver.quit()

   driver = SetUpDetails.init_driver()
   global wait
   wait = WebDriverWait(driver, 30)
   driver.get(urlName)

def fnSetValue(Locator_Value,Input_Value):
         elementUserName = wait.until(
         expected_conditions.visibility_of_element_located((By.XPATH,Locator_Value)))
         elementUserName.send_keys(Input_Value)

def fnClickObject(locatorObjectKey):
        elementToClick = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,locatorObjectKey)))
        elementToClick.click()

def fnAssertValidation(locatorAssert,assertValue):
        elementToVerify = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,locatorAssert)))

        if elementToVerify.text==assertValue:
            assert True
        else:
            assert False

def fnGetLocatorValue(Application_Type,Locator_Key):
    Temp_Dict = oGlobalLocatorDict[Application_Type]
    Locator_Value = Temp_Dict[Locator_Key]
    return Locator_Value