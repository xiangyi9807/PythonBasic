from openpyxl import Workbook

wb = Workbook()

sheet = wb.create_sheet("Sheet1")

# 删除sheet
wb.remove(sheet)

wb.save("excel_test_4.xlsx")
