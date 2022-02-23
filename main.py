from openpyxl import load_workbook

book = load_workbook('xBotParts.xlsx')

book['Plan1']['C12'] = '05-0800-02'

print(book['Plan1']['C12'].value)
print(book.save(filename='05-0800-02.xlsx'))