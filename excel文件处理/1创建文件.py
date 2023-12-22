from openpyxl import Workbook

# 实例化（在内存里创建文件）
wb = Workbook()

# 获取当前sheet
sheet = wb.active

# 保存excel
wb.save("excel_test_1.xlsx")


# 打印sheet名
print(sheet.title)

# 修改sheet名
sheet.title = "Test"
print(sheet.title)