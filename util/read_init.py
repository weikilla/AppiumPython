# coding=utf-8
# 操作ini的工具
import ConfigParser


class ReadIni:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = '/Users/wei/Documents/PythonTest/AppiumPython/config/LocalElement.ini'
        else:
            self.file_path = file_path
        self.data = self.read_ini()

    def read_ini(self):
        internal_read_ini = ConfigParser.ConfigParser()
        internal_read_ini.read(self.file_path)
        return internal_read_ini

    # 通过key获取对应的value
    def get_value(self, key, section=None):
        if section is None:
            section = 'login_element'
        # noinspection PyBroadException
        try:
            value = self.data.get(section, key)
        except:
            value = None
        return value


if __name__ == '__main__':
    read_ini = ReadIni()
    print read_ini.get_value("username")
