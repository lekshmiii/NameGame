# NameGame
The automation test cases are designed in Pytest Framework using the Page object model approach
Allure framework is used to generate reports that can be viewed in browser.
The Test cases are in the file named "test_NameGame.py" inside the "tests" package in the project.All other packages and folders support the execution
of the test_NameGame.py file. Instructions to run automation tests
1) The tests have been executed in macOS Mojave Version 10.14.6

2) Install Python . The tests have been executed with pycharm version 3.7.3

3) Download the “NameGame” project from GitHub

4) If running on chrome ,chromedriver should be installed and path mentioned in the Testdata.py file (chrome_webdriver = “xxx”) .
The tests have been executed with chrome Version 89.0.4389.90 (Official Build) (x86_64)

5) If running on safari ,safari webdriver should be installed and path mentioned in the Testdata.py file (safari_webdriver = “xxx”) .
The tests have been executed with chrome Version 14.0.3 (14610.4.3.1.7)

6) Install all dependancies to the project using the below
command:
python -m pip install -r requirements.txt.
Or
pip install -r requirements.txt

7) Run the test cases using below command and it generates reports in Reports directory pytest <absolute path of the test file> --alluredir ./Reports
example:

 pytest /Users/XXX/PycharmProjects/NameGame/tests/test_NameGame.py -- alluredir ./Reports
 
8) To see the results
command:
"allure serve <absolute path of the "Reports" directory>” Example:
allure serve /Users/XXX/PycharmProjects/NameGame/Reports

9) "control + C" to exit
