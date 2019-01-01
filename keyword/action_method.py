# coding=utf-8
import time

from util.get_by_local import GetByLocal
from base.base_driver import BaseDriver


class ActionMethod:
    """
    封装操作函数类
    """
    def __init__(self):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(0)
        self.get_by_local = GetByLocal(self.driver)

    def input(self, element_key, value):
        """
        操作输入值的元素
        :param element_key:
        :param value:
        :return:
        """
        element = self.get_by_local.get_element(element_key)
        if element is None:
            return element_key, "元素没找到"
        element.sendkeys(value)

    def on_click(self, element_key):
        """
         操作可点击的元素
        :param element_key:
        :return:
        """
        element = self.get_by_local.get_element(element_key)
        if element is None:
            return element_key, "元素没找到"
        element.click()

    def sleep_time(self, value):
        time.sleep(value)

    # 获取屏幕的宽高
    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左边滑动
    def swipe_left(self):
        # [100,200]
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x, y1, 2000)

    # 向右边滑动
    def swipe_right(self):
        # [100,200]
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        self.driver.swipe(x1, y1, x, y1, 2000)

    # 向上滑动
    def swipe_up(self):
        # [100,200]direct ion
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 9
        y = self.get_size()[1] / 10
        self.driver.swipe(x1, y1, x1, y, 1000)

    # 向下滑动
    def swipe_down(self):
        # [100,200]
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
        driver.swipe(x1, y1, x1, y)
