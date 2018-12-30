#     7.action
#     点击百度(记得退出用户 )-需要把鼠标移动到更多产品-选择百度音乐
# """

# #7.使用action打开   点击百度(记得退出用户 )-需要把鼠标移动到更多产品-选择百度音乐
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import unittest
# import time
# class Cnode(unittest.TestCase):
#     def setUp(self):
#         self.url = 'https://www.baidu.com'
#         self.driver = webdriver.Chrome()
#         self.driver.get(self.url)

#     def testmusic(self):
#         driver = self.driver
#         #第一种：
#         # driver.find_element_by_link_text('更多产品').click()
#         # driver.find_element_by_link_text('音乐').click()
#         #第二种：
#         c = driver.find_element_by_css_selector('a[name=tj_briicon]')
#         ActionChains(driver).move_to_element(c).perform()
#         h = driver.find_element_by_xpath('//div[4]/div/div[2]/div[1]/div/a[2]')
#         ActionChains(driver).move_to_element(h).click().perform()

#     def tearDown(self):
#         driver = self.driver
#         driver.save_screenshot('./music.png')
#         time.sleep(3)
#         driver.quit()
# if __name__ == "__main__":
#     unittest.main()