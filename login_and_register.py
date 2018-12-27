#20181227¡ª¡ªÐ´Ò»¸öµÇÂ½×¢²á
#ÍøÖ·£ºhttp://39.107.96.138:3000/signup
#Áù.
import unittest
import time
from selenium import webdriver
class Cnode(unittest.TestCase):

    def setUp(self):
        self.url = 'http://39.107.96.138:3000'
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def test_login(self):
        driver = self.driver
        driver.find_element_by_css_selector('a[href="/signin"]').click()
        driver.find_element_by_id('name').send_keys('test01')
        driver.find_element_by_id('pass').send_keys('123456')
        driver.find_element_by_class_name('span-primary').click()

    def test_register(self):
        driver = self.driver
        driver.find_element_by_css_selector('a[href="/signup"]').click()
        driver.find_element_by_id('loginname').send_keys('chenghong')
        driver.find_element_by_id('pass').send_keys('123456')
        driver.find_element_by_id('re_pass').send_keys('1234567')
        driver.find_element_by_id('email').send_keys('qwerty')
        driver.find_element_by_class_name('span-primary').click() 

    def tearDown(self):
        self.driver.save_screenshot('./01.png')
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()