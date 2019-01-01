# coding=utf-8
import time
import sys
from appium import webdriver
from util.read_init import ReadIni
from util.get_by_local import GetByLocal

sys.path.append('/Users/wei/Documents/PythonTest/AppiumPython')


def get_driver():
    capabilities = {
        "platformName": "Android",
        # "automationName":"UiAutomator2",
        "deviceName": "127.0.0.1:4723",
        "app": "/Users/wei/Documents/PythonTest/AppiumPython/mukewang.apk",
        "appWaitActivity": "cn.com.open.mooc.user.login.MCLoginActivity",
        "noReset": "true"
    }
    internal_river = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    return internal_river


# 获取屏幕的宽高
def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width, height


def login():
    get_by_local = GetByLocal(driver)
    get_by_local.get_element('username').send_keys('15160047541')
    get_by_local.get_element('password').send_keys('1228763174love')
    get_by_local.get_element('login_button').click()


driver = get_driver()
login()
