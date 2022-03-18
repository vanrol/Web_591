# !/usr/env python 3
# -*- coding: utf-8 -*-

from public.utils.locating import find_class_name, find_xpath, find_css, finds_css, finds_xpath, find_id, find_link_text
from selenium import webdriver
import time
import pytest
import allure
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
import re
import itertools

# driver = webdriver.Chrome()
# driver.implicitly_wait(8)  # 8秒的静默等待时间
# driver.get("https://sale.debug.591.com.tw/map-index.html#l11=2&l12=0&l21=12&l22=25.091075&l23=121.5598345&l31=12&l32=25.091075&l33=121.5598345&l41=24.966797469080014&l42=25.215226437026036&l43=121.30268575732423&l44=121.81698324267579&p11=undefined&p12=0&p13=0&p14=undefined&f0=0&f2=0&f3=0&f4=0&f5=0&f6=undefined&f7=undefined&f8=undefined&rid=1&sid=&price=0&minprice=0&maxprice=0&minarea=0&maxarea=0")

regions_list = ['新北市', '桃園市', '台北市', '新竹縣', '新竹市', '基隆市',
                        '宜蘭縣', '台中市', '苗栗縣', '彰化縣', '南投縣', '雲林縣',
                        '高雄市', '台南市', '屏東縣', '嘉義市', '嘉義縣', '花蓮縣',
                        '台東縣', '金門縣', '澎湖縣', '連江縣']
kinds_list = ['不限', '住宅', '套房', '法拍屋', '其他']
combitions = product(regions_list, kinds_list)
print(list(combitions))

def price_list(seq):
    """
    seq = 'des'時為價格降序列表
    seq = 'asc'時為價格升序列表
    """
    if seq == 'des':
        dropdown = find_id(driver, "order-select")
        find_xpath(dropdown , "//option[. = '金額從大到小']").click()
    elif seq == 'asc':
        dropdown = find_id(driver, "order-select")
        find_xpath(dropdown, "//option[. = '金額從小到大']").click()
    time.sleep(3)
    num = len(finds_css(driver, ".price"))
    price_lst = []
    for i in range (1,num+1):
        list_price = find_xpath(driver, '/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/ul/li[{}]/div[3]/em'.format(str(i))).text
        res1 = list_price.replace(',', '')
        res2 = res1.replace('萬', '')
        price_lst.append(int(res2))
    return price_lst

# 獲取金額篩選框的列表
def get_price_screen_box(region_name, kind_name):
    price_box_list = []
    # 篩選城市
    find_id(driver, "regionSh").click()
    find_link_text(driver, region_name).click()
    # 篩選類型
    find_id(driver, "kindSh").click()
    find_link_text(driver, kind_name).click()
    # 打開金額篩選框
    find_id(driver, "filterPriceSh").click()
    for i in range(1,8):
        for priceScreenBox in finds_xpath(driver, '/html/body/div[1]/div[1]/div[3]/div/div[3]/div[8]/ul/div[2]/li[{}]/a'.format(i)):
            price_box_list.append(priceScreenBox)
    return price_box_list

if __name__ == '__main__':
    pass