import time
from selenium import webdriver
driver = webdriver.Chrome()
def Param(url,selector,keyword):
    driver.get(url)
    if selector == 'kw':
        driver.find_element_by_id('kw').send_keys('明天，你好')
    elif selector == 'sb_form_q':
        driver.find_element_by_id('sb_form_q').send_keys('你好，明天')
Param('https://www.baidu.com','kw','keyword')
Param('https://cn.bing.com/','sb_form_q','sb_form_q')
time.sleep(5)
driver.quit()
