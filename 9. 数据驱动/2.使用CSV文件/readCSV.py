#! /usr/bin/env python
# author: vin

import csv
'''
读取：列表、字典
'''

class OperationCSV():
    @property
    def readCSVList(self):
        with open('sina.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for item in reader:
                # print(item)
                return item

    @property
    def readCSVDict(self):
        with open('sina.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for item in reader:
                print(item)
                # return item

if __name__ == '__main__':
    obj = OperationCSV()
    # obj.readCSVList
    obj.readCSVDict