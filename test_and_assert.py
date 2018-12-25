#四、text属性：拿到文本值--视频006
#如何获取网页文本
#添加判断：断言用法导入  assert
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# #打印title
# print(driver.title)
# #判断‘百度’是否在搜索结果中
# assert '百度' in driver.title
# #在文本框中输入‘吴尊’
# driver.find_element_by_id('kw').send_keys('吴尊')
# #点击搜索
# driver.find_element_by_id('su').click()
# #延时3S
# time.sleep(3)
# #使用text属性拿到文本值
# result = driver.find_element_by_id('content_left').text
# #打印文本值
# print(result)
# assert '吴尊' in result
# #把搜索到的结果保存在文本文档中‘wuzun.text’
# with open(r'wuzun.text','w',encoding = 'utf-8') as file:
#     file.write(result)
# #关闭网页
# driver.quit()