from openpyxl import load_workbook

try:
    wb = load_workbook("excel_test_2.xlsx")
except Exception as e:
    raise e