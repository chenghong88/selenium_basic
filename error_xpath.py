#4.xpath--��ÿ���ֻ��б����--����ֻ�ͼƬ  �򲻿��������
#�̶�д����[@]
"""
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=e731e1e224b9455fa7b3cfe95151ebf4')
driver.maximize_window()
result = driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]')
print('�򿪵�ҳ����',len(driver.window_handles))
for index in result:
    result = driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]')
    result[index].click()
    allwindows = driver.window_handles
    driver.switch_to.window(allwindows[1])
    time.sleep(2)
    text = driver.find_element_by_css_selector('span.price.J-p-100002332162').text
    print(text)
    driver.close()
    driver.switch_to.window(allwindows[0])
    time.sleep(2)
"""