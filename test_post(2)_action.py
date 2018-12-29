#2018.12.28——实战
#使用action进行发帖操作(方法二)
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
class Cnode(unittest.TestCase):
    def  setUp(self):
        self.url = 'http://39.107.96.138:3000'
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        driver = self.driver
        driver.find_element_by_css_selector('a[href="/signin"]').click()
        driver.find_element_by_id('name').send_keys('user0')
        driver.find_element_by_id('pass').send_keys('123456')
        driver.find_element_by_css_selector('input[type ="submit"]').click()
        
# 登陆成功后，页面导航到首页
# 发布话题的操作
# 1.首页点击发布话题 - 话题发布页面
# 2.选择一个版块
# 3.输入标题
# 4.输入文本
# 5.提交
# 请将上述5步操作在下面test_post中实现

    def  test_post_topic(self):
        driver = self.driver
        driver.find_element_by_css_selector('span[class="span-success"]').click()
        driver.find_element_by_xpath('//*[@id="tab-value"]/option[3]').click()
        driver.find_element_by_css_selector('textarea[id="title"]').send_keys('面向大海春暖花开--蓝胖子')
        #由于不是text和teartext文本，所以不能直接使用send_keys()输入文本，需要赋值给一个变量
        content_area = driver.find_element_by_class_name('[class="CodeMirror-scroll"]')
        #点击这个变量
        content_area.click()
        #使用action方法点击传入变量，再使用send_keys()输入文本，需要加上perform()，否则不会调用action方法
        #使用action方法之前需要引入包：from selenium.webdriver.common.action_chains import ActionChains
        ActionChains(driver).move_to_element(content_area).send_keys('xxxxxxxxxxxxxxxxxxxx').perform()
        driver.find_element_by_css_selector('input[type="submit"]').click()

    def tearDown(self):
        self.driver.save_screenshot('./postttopic.png')
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()