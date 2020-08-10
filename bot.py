from selenium import webdriver
from time import sleep

class Bot:
    def __init__(self, username, password):
        self.driver=webdriver.Chrome()
        self.user=username
        self.pw=password
        self.driver.get("https://www.instagram.com/")
        sleep(3)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        sleep(3)
        self.driver.find_element_by_xpath('//input[@name="password"]')\
            .send_keys(password)
        sleep(3)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(3)
        self.driver.find_element_by_xpath('//button[text()="Not Now"]').click()
        sleep(3)
        self.driver.find_element_by_xpath('//button[text()="Not Now"]').click()
        sleep(3)
        self.driver.find_element_by_xpath('//a[contains(@href, "{}")]'.format(self.user)).click()
        sleep(3)



Bot('[YOUR_INSTAGRAM_USERNAME]]', "[YOUR_INSTAGRAM_PASSWORD]")