# coding=utf-8
import unittest
import HTMLTestRunner
import threading
import multiprocessing
from business.login_business import LoginBusiness
import time
from util.server import Server
from util.write_user_command import WriteUserCommand


class ParameTestCase(unittest.TestCase):

    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        # 声明一个全局变量
        global parames
        parames = parame


class CaseTest(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        print "setUpclass---->", parames
        cls.login_business = LoginBusiness(parames)


    def setUp(self):
        print "this is setup \n"


    def test_02(self):
        print "test case 里面的参数:", parames
        self.login_business.login_pass()


    def test_01(self):
        print "this is test_01\n"
        self.login_business.login_user_error()
        self.assertTrue(True)


    def tearDown(self):
        print "this is teardown"

    @classmethod
    def tearDownClass(cls):
        print "this is teardownClass"


def appium_init():
    server = Server()
    server.main()


def get_suite(i):
    print "get_suite里面的", i
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_01", parame=i))
    suite.addTest(CaseTest("test_02", parame=i))
    # unittest.TextTestRunner().run(suite)
    html_file = "/Users/wei/Documents/PythonTest/AppiumPython/report/report" + str(i) + ".html"
    fp = file(html_file, 'wb')
    HTMLTestRunner.HTMLTestRunner(stream=fp).run(suite)


def get_count():
    write_user_file = WriteUserCommand()
    return write_user_file.get_file_line()


if __name__ == '__main__':
    appium_init()
    threads = []
    for i in range(get_count()):
        t = threading.Thread(target=get_suite,  args=(i,))
        threads.append(t)
    for j in threads:
        j.start()
        time.sleep(1)
