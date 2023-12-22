#! /usr/bin/env python
# author: vin

import openpyxl
import os

data_path = os.path.dirname(os.path.dirname(os.path.abspath('__file__'))) + '\\data\\accounts.xlsx'

try:
    wb = openpyxl.load_workbook(data_path)
except Exception as e:
    raise e

sheet = wb.active
account_dict = {}
id_list = []
name_list = []

for row in sheet.iter_rows(min_row=2, max_row=3, min_col=1, max_col=2):
    i = 1
    for cell in row:
        if i%2 != 0:
            id_list.append(cell.value)
        else:
            name_list.append(cell.value)
        i += 1

account_dict = zip(id_list, name_list)
