#! /usr/bin/env python
# author: vin

import csv
'''
写入csv: 字典、列表
'''

class OperationCSV():

    header = ['平台', '课程', '老师']
    dicts = [
        {'平台':'腾讯课程', '课程':'API实战', '老师':'Vin'},
        {'平台':'51CTO', '课程':'自动化实战', '老师':'Vin'},
    ]

    @property
    def writeListCSV(self):
        with open('weike.csv', 'w', encoding='utf-8', newline='') as f:
            w = csv.writer(f)
            w.writerow(self.header)
            for item in self.dicts:
                w.writerow(item)

    @property
    def writeDictCSV(self):
        with open('weike_dict.csv', 'w', encoding='utf-8', newline='') as f:
            w = csv.DictWriter(f, self.header)
            w.writeheader()
            for item in self.dicts:
                w.writerow(item)

if __name__ == '__main__':
    obj = OperationCSV()
    # obj.writeListCSV
    obj.writeDictCSV