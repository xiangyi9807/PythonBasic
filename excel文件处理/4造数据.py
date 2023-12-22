import string
from openpyxl import Workbook
from openpyxl import load_workbook
import random

wb = Workbook()

sheet = wb.active

sheet.append(["编号", "姓名", "年龄", "地址"])

for i in range(100):
    sheet.append([i,
                  ''.join(random.sample(string.ascii_letters + string.digits, 5)),
                  random.choice(range(50)),
                  ''.join(random.sample(string.ascii_letters + string.digits, 10))])


wb.save("excel_test_3.xlsx")