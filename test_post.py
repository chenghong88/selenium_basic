#2018.12.28——实战
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
        pass
        driver = self.driver
        driver.find_element_by_css_selector('span[class="span-success"]').click()
        c = driver.find_element_by_xpath('//*[@id="tab-value"]')
        ActionChains(driver).double_click(c).perform()
        driver.find_element_by_xpath('//*[@id="tab-value"]/option[3]').click()
        driver.find_element_by_css_selector('textarea[id="title"]').send_keys('面向大海春暖花开--蓝胖子')
        driver.find_element_by_css_selector('div[class="CodeMirror cm-s-paper"]').click()
        driver.find_element_by_xpath('//*[@id="create_topic_form"]/fieldset/div/div/div[2]/div[1]/textarea').send_keys('有些歌词总不经意的让人红了眼眶，或许因为感动；或许因为被说中了心事；也或许因为歌词刚好描述着自己的故事。')
        driver.find_element_by_css_selector('input[type="submit"]').click()

    def tearDown(self):
        self.driver.save_screenshot('./postttopic.png')
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()