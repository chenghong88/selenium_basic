#�塢keys�÷�--��Ƶ007
# Keys.ENTER
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# driver.find_element_by_id('kw').send_keys('����')
# # Keys.ENTER ���������
# driver.find_element_by_id('su').send_keys(Keys.ENTER)

#��.1��ʹ��seleniumд��Ԫ���ԣ����ʹ��unittest��--��Ƶ007
#1.���д������������test��ͷ
#2.setUp�����ǹ̶��ģ�ÿһ��������ִ��֮ǰ������ִ��setUp --�������
#3.tearDown������ÿ��test����ִ����֮�󶼻�ִ��tearDown --�ر������

# import unittest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# class Baidu_and_search(unittest.TestCase):
#     def setUp(self):
#         #���������
#         self.driver = webdriver.Chrome()
#     def test_baidu_search(self):
#         #����driver��������
#         driver = self.driver
#         driver.get('https://www.baidu.com')
#         driver.find_element_by_id('kw').send_keys('����')
#         driver.find_element_by_id('su').send_keys(Keys.ENTER)
#     def test_bing_search(self):
#         driver = self.driver
#         driver.get('https://cn.bing.com/')
#         driver.find_element_by_id('sb_form_q').send_keys('����')
#         driver.find_element_by_id('sb_form_go').send_keys(Keys.ENTER)
#     def tearDown(self):
#         #�ر������
#         time.sleep(3)
#         self.driver.quit()
# #
# if __name__ == "__main__":
#     unittest.main()