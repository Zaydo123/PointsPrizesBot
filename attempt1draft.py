from selenium import webdriver
from time import sleep
import pyautogui as pa

email = 'x'
zipnum = 12345


def launchChrome():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://pointsprizes.com")
    sleep(1)
    emailboxlogin = driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div[1]/form/div[1]/input[1]").send_keys(email)
    createacctbutton = driver.find_element_by_xpath('//*[@id="wrapper"]/div[4]/div/div/div[1]/form/div[1]/span/button').click()

def chooseSurveyPeople():
    sleep(1)
    peanut = driver.find_elements_by_class_name('img-rounded')
    peanutNumber = peanut[5]
    peanutNumber.click()
    sleep(6)

def surveyNumbaWan():
    clokTingy = pa.locateCenterOnScreen('surveyOptions.png', confidence=0.8)
    pa.click(clokTingy)
    sleep(3)
    getstarted = pa.locateCenterOnScreen('continue.PNG', confidence=0.8)
    pa.click(getstarted)
    sleep(5)
    ZipCode = driver.find_element_by_class_name('form-type1-text ng-isolate-scope ng-empty ng-dirty ng-valid-parse ng-invalid ng-invalid-required ng-touched')
    ZipCode.send_keys(zipNum)
    '''
    CountyBox = driver.find_element_by_xpath('//*[@id="ss_100263_"]')
    CountyBox.select_by_index(0)
    sleep(5)
    '''
launchChrome()
chooseSurveyPeople()
surveyNumbaWan()
