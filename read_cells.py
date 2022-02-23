from openpyxl import load_workbook

book = load_workbook('05-0800-01.Xlsx')

print(book['Sheet']['A1'].value)
print(book['Sheet']['B1'].value)