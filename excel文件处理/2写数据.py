from openpyxl import Workbook
import datetime

wb = Workbook()
sheet = wb.active
sheet.title = "Test"

# 方式一：数据直接分配到单元格
sheet["C3"] = "hello world"

# 方式二：附加行，从第一列开始附加（从最下方空白处，最左边开始，可以输入多行）
sheet.append([1, 2, 3])
sheet.append([4, 5, 6])

# 方式三：自动转换python类型
sheet["A1"] = datetime.datetime.now().strftime("%Y-%m-%d")

# 使用公式
sheet["D5"] = "=SUM(A5:C5)"

# 创建sheet
sheet = wb.create_sheet("Sheet1")
sheet["C3"] = "hello world"

# 保存文件
wb.save("excel_test_2.xlsx")