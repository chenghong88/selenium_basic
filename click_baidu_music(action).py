#     7.action
#     ����ٶ�(�ǵ��˳��û� )-��Ҫ������ƶ��������Ʒ-ѡ��ٶ�����
# """

# #7.ʹ��action��   ����ٶ�(�ǵ��˳��û� )-��Ҫ������ƶ��������Ʒ-ѡ��ٶ�����
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
#         #��һ�֣�
#         # driver.find_element_by_link_text('�����Ʒ').click()
#         # driver.find_element_by_link_text('����').click()
#         #�ڶ��֣�
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