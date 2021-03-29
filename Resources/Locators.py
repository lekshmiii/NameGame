from selenium import webdriver
from selenium.webdriver.common.by import By


# Locators_class has all the web element locators

class Locators_class():

#xpath can be generalized
    photo_xpath = "//div[@data-n = 0]"
    tries_classname = "attempts"
    correct_classname = "correct"
    streak_classname = "streak"