#�ġ�text���ԣ��õ��ı�ֵ--��Ƶ006
#��λ�ȡ��ҳ�ı�
#����жϣ������÷�����  assert
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# #��ӡtitle
# print(driver.title)
# #�жϡ��ٶȡ��Ƿ������������
# assert '�ٶ�' in driver.title
# #���ı��������롮����
# driver.find_element_by_id('kw').send_keys('����')
# #�������
# driver.find_element_by_id('su').click()
# #��ʱ3S
# time.sleep(3)
# #ʹ��text�����õ��ı�ֵ
# result = driver.find_element_by_id('content_left').text
# #��ӡ�ı�ֵ
# print(result)
# assert '����' in result
# #���������Ľ���������ı��ĵ��С�wuzun.text��
# with open(r'wuzun.text','w',encoding = 'utf-8') as file:
#     file.write(result)
# #�ر���ҳ
# driver.quit()