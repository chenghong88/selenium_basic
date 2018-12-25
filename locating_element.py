#二、定位元素有4种:
#1.通过css定位元素--视频004
#点击新闻
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# driver.find_element_by_css_selector('a[name="tj_trnews"]').click()
# time.sleep(5)
# driver.quit()

#2.通过xpath定位元素--视频004
#打开百度--输入'吴尊'
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('吴尊')
# time.sleep(5)
# driver.quit()

#3.通过name定位元素--视频003
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# driver.find_element_by_name('wd').send_keys('吴尊')
# time.sleep(4)
# driver.quit()

#4.通过 id 定位元素--视频003
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# driver.find_element_by_id('kw').send_keys('吴尊')
# time.sleep(4)
# driver.quit()