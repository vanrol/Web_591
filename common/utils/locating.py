#!/usr/bin/env python 3
# -*- coding:utf-8 -*-

from selenium import webdriver


# 定位单个元素
def find_id(driver, id):
    return driver.find_element_by_id(id)


def find_name(driver, name):
    return driver.find_element_by_name(name)


def find_class_name(driver, class_name):
    return driver.find_element_by_class_name(class_name)


def find_xpath(driver, xpath):
    return driver.find_element_by_xpath(xpath)


def find_css(driver, css):
    return driver.find_element_by_css_selector(css)


def find_link_text(driver, link_text):
    return driver.find_element_by_link_text(link_text)


def find_partial_link_text(driver, partial_link_text):
    return driver.find_element_by_partial_link_text(partial_link_text)


def find_tag_name(driver, tag_name):
    return driver.find_element_by_tag_name(tag_name)


# 定位元素组
def finds_id(driver, id):
    return driver.find_elements_by_id(id)


def finds_name(driver, name):
    return driver.find_elements_by_name(name)


def finds_class_name(driver, class_name):
    return driver.find_elements_by_class_name(class_name)


def finds_xpath(driver, xpath):
    return driver.find_elements_by_xpath(xpath)


def finds_css(driver, css):
    return driver.find_elements_by_css_selector(css)


def finds_link_text(driver, link_text):
    return driver.find_elements_by_link_text(link_text)


def finds_partial_link_text(driver, partial_link_text):
    return driver.find_elements_by_partial_link_text(partial_link_text)


def finds_tag_name(driver, tag_name):
    return driver.find_elements_by_tag_name(tag_name)
