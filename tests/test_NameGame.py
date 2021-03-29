from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import allure
from allure_commons.types import AttachmentType
from Resources.Locators import Locators_class
from Resources.Base import BaseClass
from Resources.Testdata import testdataclass


#Pytest fixture function browser() initializes the driver and yields it whenever called and also quits the driver after running a test case
@pytest.fixture()
def browser():
    driver = webdriver.Chrome(testdataclass.chrome_webdriver)
    yield driver
    driver.quit()

#Pytest fixture function locators_fixture() creates an instance of class "Locators_class" that resides in the Locators.py file
@pytest.fixture()
def locators_fixture():
    lp = Locators_class()
    return lp

#Pytest fixture function base_fixture() creates an instance of class "BaseClass" that resides in the Base.py file
@pytest.fixture()
def base_fixture(browser):
    bp = BaseClass(browser)
    return bp

#Pytest fixture function testdata_fixture() creates an instance of class "testdataclass" that resides in the Testdata.py file
@pytest.fixture()
def testdata_fixture():
    tp = testdataclass()
    return tp


#@allure.title("Name Game Test Automation Suite")
#@allure.feature("To win, user select a photo to match the name in the question ")

class Testclass:
    #1) Verifies name game title is shown
    #@pytest.mark.skip(reason="skipped")
    @allure.story("Name Game page is displayed and ready to play")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_navigatehomepage(self,browser,testdata_fixture,base_fixture):
        #url is opened
        browser.get(testdata_fixture.url)
        # wait untill the photos are loaded and displayed
        base_fixture.waitforpageload()
        print(browser.title)
        time.sleep(2)
        #verifying weather the browser title is equal to the title specified in the testdata.py file.
        #assert testdata_fixture.browser_title_partial in browser.title
        if testdata_fixture.browser_title_partial == browser.title:
            assert True
            allure.attach(browser.get_screenshot_as_png(),name="Loggedscreen has expected title",attachment_type=AttachmentType.PNG)
        else:
            allure.attach(browser.get_screenshot_as_png(),name="Loggedscreen title wrong",attachment_type=AttachmentType.PNG)
            assert False


    #2)Verify name and displayed photos change after selecting the correct answer
    #@pytest.mark.skip(reason="skipped")
    @allure.story("Name Game page is displayed and ready to play")
    @allure.severity(allure.severity_level.NORMAL)
    def test_verifyNewMatchNameAndPhotosAfterCorrectSelection(self,browser,testdata_fixture,base_fixture):
        # url is opened
        browser.get(testdata_fixture.url)
        timeout = 3
        # wait untill the photos are loaded and displayed
        base_fixture.waitforpageload()
        #Get initial list of photos and associated names, and name to match

        allure.attach(browser.get_screenshot_as_png(), name="firstmatchname and first list of photos displayed",attachment_type=AttachmentType.PNG)

        originalPhotos = browser.find_elements(By.CLASS_NAME,"photo")
        originalMatchName = browser.find_element(By.ID,"name").text

        #click on correct selection of photo
        base_fixture.pickCorrectOrIncorrectPhoto("correct")
        time.sleep(10)

        allure.attach(browser.get_screenshot_as_png(), name="Newmatchname and new list of photos displayed",attachment_type=AttachmentType.PNG)

        # Get final list of photos and associated names, and name to match after clicking on correct photo
        newPhotos = browser.find_elements(By.CLASS_NAME,"photo")
        newMatchName = browser.find_element(By.ID,"name").text
        time.sleep(10)

        #verifying weather photo to be matched in question 1 is not same as the photo to be matched in question 2
        #assert originalMatchName != newMatchName

        if originalMatchName != newMatchName:
            assert True
            allure.attach(browser.get_screenshot_as_png(),name="Newmatchname is not repeated consequently",attachment_type=AttachmentType.PNG)
        else:
            allure.attach(browser.get_screenshot_as_png(),name="Newmatchname is repeated in consequent game",attachment_type=AttachmentType.PNG)
            assert False
        # verifying weather list of photos in question 1 is not same as the list of photos in question 2
        #assert originalPhotos != newPhotos

        if originalPhotos != newPhotos:
            assert True
            allure.attach(browser.get_screenshot_as_png(), name="photos in question 1 not repeated in question 2",
                          attachment_type=AttachmentType.PNG)
        else:
            allure.attach(browser.get_screenshot_as_png(), name="photos in question 1 repeated in question 2",
                          attachment_type=AttachmentType.PNG)
            assert False

    #3) Verifies “attempts”counter is incremented
    #@pytest.mark.skip(reason="skipped")
    @allure.story("Attempts , Correct and streak Counters are updated based on the correct or incorrect photo selection")
    @allure.severity(allure.severity_level.NORMAL)
    def test_validateClickingFirstPhotoIncreasesTriesCounter(self,browser,testdata_fixture,locators_fixture,base_fixture):
        # url is opened
        browser.get(testdata_fixture.url)
        timeout = 3

        # wait untill the photos are loaded and displayed
        base_fixture.waitforpageload()

        allure.attach(browser.get_screenshot_as_png(), name="initial value of tries counter",attachment_type=AttachmentType.PNG)
        #finding the initial value of tries counter
        tries = (base_fixture.triescounter_text())
        browser.find_element_by_xpath(locators_fixture.photo_xpath).click()
        time.sleep(3)

        # finding the final value of tries counter after the photo click
        allure.attach(browser.get_screenshot_as_png(), name="final value of tries counter",attachment_type=AttachmentType.PNG)
        tries_After =  (base_fixture.triescounter_text())
        #verifying that the tries counter is incremented by 1 after clicking on a photo
        #assert tries_After == tries + 1

        if tries_After == tries + 1:
            assert True
            allure.attach(browser.get_screenshot_as_png(), name="final value of tries counter incremented by 1",
                          attachment_type=AttachmentType.PNG)
        else:
            allure.attach(browser.get_screenshot_as_png(), name="final value of tries counter not incremented by 1",
                          attachment_type=AttachmentType.PNG)
            assert False




    #4) Verify that the correct counters are being incremented for tries and correct counters
    #@pytest.mark.skip(reason="skipped")
    @allure.story("Attempts , Correct and streak Counters are updated based on the correct or incorrect photo selection")
    @allure.severity(allure.severity_level.NORMAL)
    def test_verifyCorrectandTriesCountersIncrementedAsExpected(self,browser,testdata_fixture,base_fixture,locators_fixture):
        # url is opened
        browser.get(testdata_fixture.url)
        timeout = 3
        # wait untill the photos are loaded and displayed
        base_fixture.waitforpageload()

        allure.attach(browser.get_screenshot_as_png(), name="initial value of correct and tries counter",
                      attachment_type=AttachmentType.PNG)
        #finding the initial values of correct and tries counter
        tries = (base_fixture.triescounter_text())
        #verifying if the tries counter text is initially at 0
        #assert tries == 0
        if tries == 0:
            assert True
            allure.attach(browser.get_screenshot_as_png(), name="initial value of tries counter is 0",
                          attachment_type=AttachmentType.PNG)
        else:
            allure.attach(browser.get_screenshot_as_png(), name="initial value of tries counter is not 0",
                          attachment_type=AttachmentType.PNG)
            assert False

        time.sleep(2)
        correct = base_fixture.correctcounter_text()
        # verifying if the correct counter text is initially at 0
        #assert correct == 0
        if correct == 0:
            assert True
            allure.attach(browser.get_screenshot_as_png(), name="initial value of correct counter is 0",
                          attachment_type=AttachmentType.PNG)
        else:
            allure.attach(browser.get_screenshot_as_png(), name="initial value of correct counter is not 0",
                          attachment_type=AttachmentType.PNG)
            assert False

        time.sleep(2)

        #selecting an incorrect photo
        base_fixture.pickCorrectOrIncorrectPhoto("incorrect")
        time.sleep(3)

        allure.attach(browser.get_screenshot_as_png(), name="value of correct and tries counter after an incorrect selection of photo",
                      attachment_type=AttachmentType.PNG)
        #finding the values of correct and tries counter after picking an incorrect photo
        triesAfter1 = (base_fixture.triescounter_text())
        # verifying if the tries counter text is incremented after an incorrect photo selection
        #assert triesAfter1 == tries + 1

        if triesAfter1 == tries + 1:
            assert True
            allure.attach(browser.get_screenshot_as_png(), name="tries counter is incremented after an incorrect photo selection",
                          attachment_type=AttachmentType.PNG)
        else:
            allure.attach(browser.get_screenshot_as_png(), name="tries counter is not incremented after an incorrect photo selection",
                          attachment_type=AttachmentType.PNG)
            assert False


        time.sleep(2)
        correctAfter1 = base_fixture.correctcounter_text()
        # verifying if the correct counter text is not incremented after an incorrect photo selection
        #assert correctAfter1 == correct
        if correctAfter1 == correct:
            assert True
            allure.attach(browser.get_screenshot_as_png(), name="correct counter is not incremented after an incorrect photo selection",
                          attachment_type=AttachmentType.PNG)
        else:
            allure.attach(browser.get_screenshot_as_png(), name="correct counter is incremented after an incorrect photo selection",
                          attachment_type=AttachmentType.PNG)
            assert False

        time.sleep(2)
        # selecting a correct photo
        base_fixture.pickCorrectOrIncorrectPhoto("correct")
        time.sleep(3)

        allure.attach(browser.get_screenshot_as_png(),
                      name="value of correct and tries counter after a correct selection of photo",
                      attachment_type=AttachmentType.PNG)
        # finding the values of correct and tries counter after picking a correct photo
        triesAfter2 = (base_fixture.triescounter_text())
        # verifying if the tries counter text is incremented after a correct photo selection
        #assert triesAfter2 == triesAfter1 +1
        if triesAfter2 == triesAfter1 + 1:
            assert True
            allure.attach(browser.get_screenshot_as_png(), name="tries counter is incremented after a correct photo selection",
                          attachment_type=AttachmentType.PNG)
        else:
            allure.attach(browser.get_screenshot_as_png(), name="tries counter is not incremented after a correct photo selection",
                          attachment_type=AttachmentType.PNG)
            assert False

        time.sleep(2)
        correctAfter2 = base_fixture.correctcounter_text()
        # verifying if the correct counter text is incremented after a correct photo selection
        #assert correctAfter2 == correctAfter1 + 1

        if correctAfter2 == correctAfter1 + 1:
            assert True
            allure.attach(browser.get_screenshot_as_png(),name="correct counter is incremented after a correct photo selection",
                          attachment_type=AttachmentType.PNG)
        else:
            allure.attach(browser.get_screenshot_as_png(),name="correct counter is incremented after a correct photo selection",
                          attachment_type=AttachmentType.PNG)
            assert False

        time.sleep(2)


    #5) Verify the "streak" counter is incrementing on correct selections
    @allure.story("Attempts , Correct and streak Counters are updated based on the correct or incorrect photo selection")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skip(reason="this test is going to to skipped because of an existing defect")
    def test_verifystreakcountersetcorrectly(self,browser,testdata_fixture,base_fixture,locators_fixture):
        # url is opened
        browser.get(testdata_fixture.url)
        # wait untill the photos are loaded and displayed
        base_fixture.waitforpageload()
        # finding the initial value of streak counter
        streak = (base_fixture.streakcounter_text())
        # verifying if the streak counter text is initially at 0
        assert streak == 0
        time.sleep(2)

        # selecting a correct photo
        base_fixture.pickCorrectOrIncorrectPhoto("correct")
        time.sleep(3)

        # finding the values of streak counter after picking a correct photo
        streakAfter1 = (base_fixture.streakcounter_text())
        # verifying if the streak counter text is incremented after a correct photo selection
        assert streakAfter1 == streak
        time.sleep(2)

        # selecting a correct photo
        base_fixture.pickCorrectOrIncorrectPhoto("correct")
        time.sleep(3)

        # finding the values of streak counter after picking a correct photo
        streakAfter2 = (base_fixture.streakcounter_text())
        # verifying if the streak counter text is incremented after a correct photo selection
        assert streakAfter2 == streakAfter1 + 1
        time.sleep(2)


    #6) Verify the multiple “streak” counter resets after getting an incorrect answer
    @allure.story("Attempts , Correct and streak Counters are updated based on the correct or incorrect photo selection")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skip(reason="this test is going to to skipped because of an existing defect")
    def test_verifystreakcounterresetcorrectly(self,browser,testdata_fixture,base_fixture,locators_fixture):
        # url is opened
        browser.get(testdata_fixture.url)
        # wait untill the photos are loaded and displayed
        base_fixture.waitforpageload()
        # finding the initial value of streak counter
        streak = (base_fixture.streakcounter_text())
        # verifying if the streak counter text is initially at 0
        assert streak == 0
        time.sleep(2)

        # selecting a correct photo
        base_fixture.pickCorrectOrIncorrectPhoto("correct")
        time.sleep(3)

        # finding the values of streak counter after picking a correct photo
        streakAfter1 = (base_fixture.streakcounter_text())
        # verifying if the streak counter text is incremented after a correct photo selection
        assert streakAfter1 == streak
        time.sleep(2)

        # selecting a correct photo
        base_fixture.pickCorrectOrIncorrectPhoto("correct")
        time.sleep(3)

        # finding the values of streak counter after picking a correct photo
        streakAfter2 = (base_fixture.streakcounter_text())
        # verifying if the streak counter text is incremented after a correct photo selection
        assert streakAfter2 == streakAfter1 + 1
        time.sleep(2)

        #selecting an incorrect photo
        base_fixture.pickCorrectOrIncorrectPhoto("incorrect")
        time.sleep(3)

        # finding the values of streak counter after picking an incorrect photo
        streakAfter3 = (base_fixture.streakcounter_text())
        # verifying if the streak counter text is reset after an incorrect photo selection
        assert streakAfter3 == 0
        time.sleep(2)