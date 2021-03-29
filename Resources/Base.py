from selenium import webdriver
from selenium.webdriver.common.by import By
from Resources.Locators import Locators_class
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Resources.Locators import Locators_class
from Resources.Testdata import testdataclass


# BaseClass has all the reusable functions
class BaseClass():


    def __init__(self,driver):
        self.driver = driver

    def pickCorrectOrIncorrectPhoto(self,whatToPick):
        nameToMatch = self.driver.find_element(By.ID, "name").text
        print("Name to match:" + nameToMatch)
        photos = self.driver.find_elements(By.CLASS_NAME, "photo")
        print(photos)
        photoName = []
        for i in photos:
            photoName.append(i.find_element(By.CLASS_NAME, "name").text)
        print(photoName)
        time.sleep(3)
        if whatToPick == "correct":
            for j in photoName:
                new_string = j.replace("'", "")
                print(new_string)
                if new_string == nameToMatch:
                    path = self.driver.find_element_by_xpath("//*[contains(text(), '%s')]//parent::div[@class ='photo']" % j)
                    print(path)
                    path.click()
                    time.sleep(5)
                    break
                else:
                    continue

        else:
            for j in photoName:
                new_string = j.replace("'", "")
                print(new_string)
                if new_string != nameToMatch:
                    path = self.driver.find_element_by_xpath("//*[contains(text(), '%s')]//parent::div[@class ='photo']" % j)
                    print(path)
                    path.click()
                    time.sleep(5)
                    break
                else:
                    continue


    def triescounter_text(self):
        tries = self.driver.find_element(By.CLASS_NAME, Locators_class.tries_classname).text
        int_tries = int(tries)
        print(int_tries)
        return int_tries

    def correctcounter_text(self):
        correct = self.driver.find_element(By.CLASS_NAME, Locators_class.correct_classname).text
        int_correct = int(correct)
        print(int_correct)
        return int_correct

    def streakcounter_text(self):
        streak = self.driver.find_element(By.CLASS_NAME, Locators_class.streak_classname).text
        int_streak = int(streak)
        print(int_streak)
        return int_streak

    def waitforpageload(self):
        timeout = 3
        # wait untill the photos are loaded and displayed
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'photo'))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        finally:
            print("Page loaded")
        time.sleep(5)