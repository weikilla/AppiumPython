# coding=utf-8
import xlrd


class OperaExcel:
    def __init__(self, file_path=None, i=None):
        """
        构造函数
        :param file_path:
        :param i:
        """
        if file_path is None:
            self.file_path = '/Users/wei/Documents/PythonTest/AppiumPython/config/case.xlsx'
        else:
            self.file_path = file_path
        if i is None:
            i = 0
        self.excel = self.get_excel()
        self.data = self.get_sheets(i)

    def get_excel(self):
        """
        获取excel文件
        :return:
        """
        excel = xlrd.open_workbook(self.file_path)
        return excel

    def get_sheets(self, i):
        """
        获取excel中的sheet
        :param i:
        :return:
        """
        tables = self.excel.sheets()[i]
        return tables

    def get_lines(self):
        """
        获取excel行数
        :return:
        """
        lines = self.data.nrows
        return lines

    def get_cell(self, row, cell):
        """
        获取单元格
        :param row:
        :param cell:
        :return:
        """
        data = self.data.cell(row, cell).value
        return data


if __name__ == '__main__':
    opera = OperaExcel()
    print opera.get_cell(2, 3)
    print opera.get_lines()
