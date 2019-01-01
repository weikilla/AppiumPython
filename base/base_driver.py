# coding=utf-8
import time
from appium import webdriver
from util.write_user_command import WriteUserCommand


class BaseDriver:
    def android_driver(self, i):
        write_file = WriteUserCommand()
        device = write_file.get_value('user_info_'+str(i), 'deviceName')
        port = write_file.get_value('user_info_'+str(i), 'port')
        capabilities = {
            "platformName": "Android",
            # "automationName":"UiAutomator2",
            "deviceName": device,
            "app": "/Users/wei/Documents/PythonTest/AppiumPython/mukewang.apk",
            "appWaitActivity": "cn.com.open.mooc.user.login.MCLoginActivity",
            "noReset": "true"
        }
        driver = webdriver.Remote("http://127.0.0.1:"+str(port)+"/wd/hub", capabilities)
        time.sleep(10)
        return driver
