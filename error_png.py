import requests,base64
from selenium import webdriver
import time

# 在公积金网上找到图片验证码这一个元素
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
# access_token = '#####调用鉴权接口获取的token#####'
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + access_token
# 二进制方式打开图文件
f = open(r'./image0.png','rb')
# 参数image：图像base64编码
img = base64.b64encode(f.read())
params = {'image':img}
imageres = requests.post(url,data=params)
image_json = imageres.json()
print(image_json)

image_num = image_json['words_result'][0]['words']
driver.find_element_by_id('imagecode1').send_keys(image_num)