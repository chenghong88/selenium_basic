import requests,base64
from selenium import webdriver
import time

# �ڹ����������ҵ�ͼƬ��֤����һ��Ԫ��
driver = webdriver.Chrome()
driver.get('https://persons.shgjj.com/')
time.sleep(2)
image_ele = driver.find_element_by_id('img1')

image_ele.screenshot(r'./image0.png')

host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=mMb2TuuX9cxwyVEX1IzAwnnV&client_secret=f5vdWx99RBoqXt3kc819InSaS0ekxKrQ'
res = requests.get(host)
r = res.json()
print(r)
access_token = r['access_token']
print(access_token)
# access_token = '#####���ü�Ȩ�ӿڻ�ȡ��token#####'
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + access_token
# �����Ʒ�ʽ��ͼ�ļ�
f = open(r'./image0.png','rb')
# ����image��ͼ��base64����
img = base64.b64encode(f.read())
params = {'image':img}
imageres = requests.post(url,data=params)
image_json = imageres.json()
print(image_json)

image_num = image_json['words_result'][0]['words']
driver.find_element_by_id('imagecode1').send_keys(image_num)