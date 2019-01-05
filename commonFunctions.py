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

def fnSetValue(locatorKey,LocatorValue):
         elementUserName = wait.until(
         expected_conditions.visibility_of_element_located((By.XPATH, oGlobalLocatorDict[locatorKey])))
         elementUserName.send_keys(LocatorValue)

def fnClickObject(locatorObjectKey):
        elementToClick = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,oGlobalLocatorDict[locatorObjectKey])))
        elementToClick.click()

def fnAssertValidation(locatorAssert,assertValue):
        elementToVerify = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,oGlobalLocatorDict[locatorAssert])))

        if elementToVerify.text==assertValue:
            assert True
        else:
            assert False
