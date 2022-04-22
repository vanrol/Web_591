# !/usr/env python 3
# -*- coding: utf-8 -*-

from common.utils.locating import find_xpath, find_css, find_link_text
from selenium.common.exceptions import NoSuchElementException
from common.utils.driver import RunDriver


class SaleFilterScreen(object):
    def __init__(self, driver):
        self.driver = driver

    def select_location(self, region_name, section_name='不限'):
        """选择城市以及縣區,不傳入縣區則默認選擇城市不限縣區"""
        find_css(self.driver, ".j-region.filter-location-btn-txt").click()
        find_link_text(self.driver, region_name).click()
        if section_name == '不限':
            find_xpath(self.driver,
                       "/html/body/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[3]/div/div[1]").click()
        else:
            find_link_text(self.driver, section_name).click()
            find_css(self.driver, '.house-switch-item.pull-left.z-select').click()

    def select_kind(self, kind_name):
        """选择房屋类型"""
        if kind_name == '不限':
            find_xpath(self.driver, '/html/body/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/a').click()
        else:
            find_link_text(self.driver, kind_name).click()

    def selcet_price(self, price_num):
        """
        :param price_num: 指代第幾個區間，從左到右共7個
        :return: 返回該價格區間元素
        """
        price_el = find_xpath(self.driver,
                              "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[{}]/a".format(price_num))
        return price_el

    def close_popbox(self):
        """關閉廣告彈窗"""
        popbox = find_css(self.driver, '.tips-popbox-img')
        try:
            popbox.click()
        except NoSuchElementException:
            pass

    def regions_list(self):
        regions_list = ['新北市', '桃園市', '台北市', '新竹縣', '新竹市', '基隆市',
                        '宜蘭縣', '台中市', '苗栗縣', '彰化縣', '南投縣', '雲林縣',
                        '高雄市', '台南市', '屏東縣', '嘉義市', '嘉義縣', '花蓮縣',
                        '台東縣', '金門縣', '澎湖縣', '連江縣']
        return regions_list

    def kinds_list(self):
        kinds_list = ['不限', '住宅', '套房', '法拍屋', '其他']
        return kinds_list

    def kinds_price01(self):
        price_dic = {'不限': ['1000萬以下', '1000-1500萬', '1500-2000萬', '2000-3000萬', '3000-4000萬', '4000-5000萬', '5000萬以上'],
                     '住宅': ['1000萬以下', '1000-1500萬', '1500-2000萬', '2000-3000萬', '3000-4000萬', '4000-5000萬', '5000萬以上'],
                     '套房': ['1000萬以下', '1000-1500萬', '1500-2000萬', '2000-3000萬', '3000-4000萬', '4000-5000萬', '5000萬以上'],
                     '法拍屋': ['1000萬以下', '1000-1500萬', '1500-2000萬', '2000-3000萬', '3000-4000萬', '4000-5000萬', '5000萬以上'],
                     '其他': ['1000萬以下', '1000-1500萬', '1500-2000萬', '2000-3000萬', '3000-4000萬', '4000-5000萬', '5000萬以上']
                     }
        return price_dic

    def kinds_price02(self):
        price_dic = {'不限': ['750萬以下', '750-1000萬', '1000-1250萬', '1250-1500萬', '1500-2000萬', '2000-3000萬', '3000萬以上'],
                     '住宅': ['750萬以下', '750-1000萬', '1000-1250萬', '1250-1500萬', '1500-2000萬', '2000-3000萬', '3000萬以上'],
                     '套房': ['750萬以下', '750-1000萬', '1000-1250萬', '1250-1500萬', '1500-2000萬', '2000-3000萬', '3000萬以上'],
                     '法拍屋': ['750萬以下', '750-1000萬', '1000-1250萬', '1250-1500萬', '1500-2000萬', '2000-3000萬', '3000萬以上'],
                     '其他': ['750萬以下', '750-1000萬', '1000-1250萬', '1250-1500萬', '1500-2000萬', '2000-3000萬', '3000萬以上'],
                     }
        return price_dic

    def kinds_price03(self):
        price_dic = {'不限': ['500萬以下', '500-750萬', '750-1000萬', '1000-1250萬', '1250-1500萬', '1500-2000萬', '2000萬以上'],
                     '住宅': ['500萬以下', '500-750萬', '750-1000萬', '1000-1250萬', '1250-1500萬', '1500-2000萬', '2000萬以上'],
                     '套房': ['500萬以下', '500-750萬', '750-1000萬', '1000-1250萬', '1250-1500萬', '1500-2000萬', '2000萬以上'],
                     '法拍屋': ['500萬以下', '500-750萬', '750-1000萬', '1000-1250萬', '1250-1500萬', '1500-2000萬', '2000萬以上'],
                     '其他': ['500萬以下', '500-750萬', '750-1000萬', '1000-1250萬', '1250-1500萬', '1500-2000萬', '2000萬以上'],
                     }
        return price_dic


if __name__ == "__main__":
    driver = RunDriver().open_page('https://sale.591.com.tw/')
    filter = SaleFilterScreen(driver)
    filter.close_popbox()
    filter.select_location('桃園市')
