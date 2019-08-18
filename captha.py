# -*- coding: utf-8 -*-

from selenium import webdriver
from application import dom_shadow

def test_captha_chek():
    driver = webdriver.Chrome(executable_path="C:\\webdriver\\chromedriver.exe")

    driver.get("https://login.mts.ru/amserver/UI/Login?service=login")

    dom_shadow(driver, "1231231232")

    driver.find_element_by_tag_name('mts-button').click()

    dom_shadow(driver, "2312")
    dom_shadow(driver, "1232")
    dom_shadow(driver, "1111")

    assert driver.find_element_by_id("captcha-image")
