
# def add(x):
#     def inner(y):
#         return x+y
#     return inner
#

# print(add(4)(5))
#    add定义一个方法，包含一个参数，inner定义另一个方法，定义一个参数，并返回一个

# from selenium import webdriver
#
# wd = webdriver.Chrome()
# wd.get('http://www.baidu.com')
import re
import requests

reo = requests.get('http://www.97xs.net/1/1729/806493.html')
sme = re.findall('htmlContent(.{0,10000000})"',reo.text)
s
print(sme)
# print(reo.text)

    




