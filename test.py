from openpyxl import load_workbook

wb = load_workbook(r"C:\Users\Baga\Desktop\Пример.xlsx")
ws = wb['Лист1']

last_row = ws.max_row
free_row = last_row + 1


for col, value in enumerate(["huh"], start=1):
    ws.cell(row=free_row, column=col, value=value)

wb.save(r"C:\Users\Baga\Desktop\Пример.xlsx")
wb.close()