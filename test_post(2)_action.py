#2018.12.28����ʵս
#ʹ��action���з�������(������)
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
        
# ��½�ɹ���ҳ�浼������ҳ
# ��������Ĳ���
# 1.��ҳ����������� - ���ⷢ��ҳ��
# 2.ѡ��һ�����
# 3.�������
# 4.�����ı�
# 5.�ύ
# �뽫����5������������test_post��ʵ��

    def  test_post_topic(self):
        driver = self.driver
        driver.find_element_by_css_selector('span[class="span-success"]').click()
        driver.find_element_by_xpath('//*[@id="tab-value"]/option[3]').click()
        driver.find_element_by_css_selector('textarea[id="title"]').send_keys('����󺣴�ů����--������')
        #���ڲ���text��teartext�ı������Բ���ֱ��ʹ��send_keys()�����ı�����Ҫ��ֵ��һ������
        content_area = driver.find_element_by_class_name('[class="CodeMirror-scroll"]')
        #����������
        content_area.click()
        #ʹ��action������������������ʹ��send_keys()�����ı�����Ҫ����perform()�����򲻻����action����
        #ʹ��action����֮ǰ��Ҫ�������from selenium.webdriver.common.action_chains import ActionChains
        ActionChains(driver).move_to_element(content_area).send_keys('xxxxxxxxxxxxxxxxxxxx').perform()
        driver.find_element_by_css_selector('input[type="submit"]').click()

    def tearDown(self):
        self.driver.save_screenshot('./postttopic.png')
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()