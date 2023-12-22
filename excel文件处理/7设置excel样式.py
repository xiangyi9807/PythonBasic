from openpyxl import Workbook
from openpyxl.styles import Font, colors, Alignment, Border, Side

wb = Workbook()

# 设置字体样式
font_style = Font(name="等线", size=24, italic=True, color=colors.BLUE, bold=True)

# 应用到sheet
sheet = wb.create_sheet("Sheet1")
sheet["A1"] = "hello world!"
sheet["A1"].font = font_style

# 设置垂直居中和水平居中
sheet["C3"] = "Python"
sheet["C3"].alignment = Alignment(vertical="center", horizontal="center")

# 设置第一行的行高
sheet.row_dimensions[1].height = 50
# 设置第三列的列宽
sheet.column_dimensions["C"].width = 50

# border
border = Border(left=Side(border_style='medium', color=colors.BLUE),
                right=Side(border_style="medium", color=colors.BLACK),
                top=Side(border_style="medium", color=colors.BLUE),
                bottom=Side(border_style="medium", color=colors.BLACK),
                diagonal=Side(border_style="medium", color=colors.BLACK),
                diagonal_direction=0,
                outline=Side(border_style="medium", color=colors.BLACK),
                vertical=Side(border_style="medium", color=colors.BLACK),
                horizontal=Side(border_style="medium", color=colors.BLACK),)
sheet["C3"].border = border

wb.save("excel_test_5.xlsx")
