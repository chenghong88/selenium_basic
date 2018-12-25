#五、keys用法--视频007
# Keys.ENTER
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# driver.find_element_by_id('kw').send_keys('吴尊')
# # Keys.ENTER 点击搜索框
# driver.find_element_by_id('su').send_keys(Keys.ENTER)

#五.1、使用selenium写单元测试：如何使用unittest库--视频007
#1.如果写方法，必须以test开头
#2.setUp方法是固定的，每一个方法在执行之前都会先执行setUp --打开浏览器
#3.tearDown方法：每个test方法执行完之后都会执行tearDown --关闭浏览器

# import unittest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# class Baidu_and_search(unittest.TestCase):
#     def setUp(self):
#         #建立浏览器
#         self.driver = webdriver.Chrome()
#     def test_baidu_search(self):
#         #创建driver（变量）
#         driver = self.driver
#         driver.get('https://www.baidu.com')
#         driver.find_element_by_id('kw').send_keys('吴尊')
#         driver.find_element_by_id('su').send_keys(Keys.ENTER)
#     def test_bing_search(self):
#         driver = self.driver
#         driver.get('https://cn.bing.com/')
#         driver.find_element_by_id('sb_form_q').send_keys('吴尊')
#         driver.find_element_by_id('sb_form_go').send_keys(Keys.ENTER)
#     def tearDown(self):
#         #关闭浏览器
#         time.sleep(3)
#         self.driver.quit()
# #
# if __name__ == "__main__":
#     unittest.main()