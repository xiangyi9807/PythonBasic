#! /usr/bin/env python
# author: vin

'''
安装第三方库 xlrd
'''

import xlrd

class OperationExcel():
    def getExcel(self):
        w = xlrd.open_workbook(filename='sina.xls')
        return w.sheet_by_index(0)  # 打开excel文件的第一个sheet

    def getRows(self):  # 获取sheet中的行
        return self.getExcel().nrows

    def getCols(self):  # 获取sheet中的列
        return self.getExcel().ncols

    def getCell(self, row, col):  # 获取sheet中的具体的单元格的值
        return self.getExcel().cell_value(row, col)

    def getEntireRow(self, row):    # 获取整行
        return self.getExcel().row_values(row)

if __name__ == '__main__':
    obj = OperationExcel()
    print(obj.getRows())
    print(obj.getCell(1,2))
    print(obj.getEntireRow(1))