# coding=utf-8
from util.get_by_local import GetByLocal
import time
from base.base_driver import BaseDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # 获取登录页面所有元素信息
    def __init__(self, i):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(i)
        self.get_by_local = GetByLocal(self.driver)

    def get_username_element(self):
        # 获取用户名元素信息
        return self.get_by_local.get_element('username')

    def get_password_element(self):
        # 获取密码元素信息
        return self.get_by_local.get_element('password')

    def get_login_button_element(self):
        return self.get_by_local.get_element('login_button')

    def get_forget_password_element(self):
        return self.get_by_local.get_element('forget_password')

    def get_register_element(self):
        return self.get_by_local.get_element('register')

    def get_toast_element(self, *args):
        time.sleep(2)
        tost_element = ("xpath", "//*[contains(@text," + args[0] + ")]")
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(tost_element))
