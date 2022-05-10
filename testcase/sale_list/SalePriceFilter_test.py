# !/usr/env python 3
# -*- coding: utf-8 -*-

import pytest
import allure
from selenium.common.exceptions import NoSuchElementException
from common.utils.driver import RunDriver
from page.sale_list_page import SaleFilterScreen

# 配置驅動
driver = RunDriver().open_page('https://sale.debug.591.com.tw/')
SaleFilterScreen = SaleFilterScreen(driver)
# 關閉覆蓋頁面的廣告
SaleFilterScreen.close_popbox()
# 獲取該頁面的城市&房屋類型數據
regions_list = SaleFilterScreen.regions_list()
kinds_list = SaleFilterScreen.kinds_list()


def region_price_data(regions_list, kinds_list):
    """獲取城市&房屋類型所有搭配的價格區間，並返回一個data"""
    region_price_data = {}
    for region_name in regions_list:
        print(region_name)
        kind_price = {}
        # 选择城市
        SaleFilterScreen.select_location(region_name, '不限')
        # 遍歷完成篩選後的價格列表
        for kind_name in kinds_list:
            price_list = []
            # 選擇類型
            SaleFilterScreen.select_kind(kind_name)
            for i in range(2, 9):
                try:
                    price_text = SaleFilterScreen.selcet_price(i).text
                    price_list.append(price_text)
                except NoSuchElementException:
                    break
            kind_price[kind_name] = price_list
        region_price_data[region_name] = kind_price
    return region_price_data

all_dic = region_price_data(regions_list, kinds_list)

@allure.feature("测试中古屋列表各城市金额筛选框的ui")
class TestRegionsPrice(object):
    def setup(self):
        self.expected_price01 = SaleFilterScreen.kinds_price01()
        self.expected_price02 = SaleFilterScreen.kinds_price02()
        self.expected_price03 = SaleFilterScreen.kinds_price03()

    @allure.story("【台北市】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_01(self):
        assert all_dic['台北市'] == self.expected_price01

    @allure.story("【基隆市】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_02(self):
        assert all_dic['基隆市'] == self.expected_price03

    @allure.story("【宜蘭縣】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_03(self):
        assert all_dic['宜蘭縣'] == self.expected_price03

    @allure.story("【苗栗縣】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_04(self):
        assert all_dic['苗栗縣'] == self.expected_price03

    @allure.story("【彰化縣】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_05(self):
        assert all_dic['彰化縣'] == self.expected_price03

    @allure.story("【南投縣】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_06(self):
        assert all_dic['南投縣'] == self.expected_price03

    @allure.story("【雲林縣】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_07(self):
        assert all_dic['雲林縣'] == self.expected_price03

    @allure.story("【高雄市】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_08(self):
        assert all_dic['高雄市'] == self.expected_price03

    @allure.story("【台南市】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_09(self):
        assert all_dic['台南市'] == self.expected_price03

    @allure.story("【屏東縣】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_10(self):
        assert all_dic['屏東縣'] == self.expected_price03

    @allure.story("【嘉義市】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_11(self):
        assert all_dic['嘉義市'] == self.expected_price03

    @allure.story("【嘉義縣】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_12(self):
        assert all_dic['嘉義縣'] == self.expected_price03

    @allure.story("【花蓮縣】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_13(self):
        assert all_dic['花蓮縣'] == self.expected_price03

    @allure.story("【台東縣】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_14(self):
        assert all_dic['台東縣'] == self.expected_price03

    @allure.story("【金門縣】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_15(self):
        assert all_dic['金門縣'] == self.expected_price03

    @allure.story("【澎湖縣】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_16(self):
        assert all_dic['澎湖縣'] == self.expected_price03

    @allure.story("【連江縣】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_17(self):
        assert all_dic['連江縣'] == self.expected_price03

    @allure.story("【新北市】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_18(self):
        assert all_dic['新北市'] == self.expected_price02

    @allure.story("【桃園市】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_19(self):
        assert all_dic['桃園市'] == self.expected_price02

    @allure.story("【新竹縣】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_20(self):
        assert all_dic['新竹縣'] == self.expected_price02

    @allure.story("【新竹市】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_21(self):
        assert all_dic['新竹市'] == self.expected_price02

    @allure.story("【台中市】住宅、套房、法拍屋、其他、不限類型房源的價格區間驗證")
    def test_22(self):
        assert all_dic['台中市'] == self.expected_price02


if __name__ == "__main__":
    pytest.main()
