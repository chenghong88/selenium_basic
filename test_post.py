#2018.12.28����ʵս
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
        pass
        driver = self.driver
        driver.find_element_by_css_selector('span[class="span-success"]').click()
        c = driver.find_element_by_xpath('//*[@id="tab-value"]')
        ActionChains(driver).double_click(c).perform()
        driver.find_element_by_xpath('//*[@id="tab-value"]/option[3]').click()
        driver.find_element_by_css_selector('textarea[id="title"]').send_keys('����󺣴�ů����--������')
        driver.find_element_by_css_selector('div[class="CodeMirror cm-s-paper"]').click()
        driver.find_element_by_xpath('//*[@id="create_topic_form"]/fieldset/div/div/div[2]/div[1]/textarea').send_keys('��Щ����ܲ���������˺����ۿ���������Ϊ�ж���������Ϊ��˵�������£�Ҳ������Ϊ��ʸպ��������Լ��Ĺ��¡�')
        driver.find_element_by_css_selector('input[type="submit"]').click()

    def tearDown(self):
        self.driver.save_screenshot('./postttopic.png')
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()