from openpyxl import load_workbook

def write_excel(filename: str, data:list[str], action: str):
    try:
        wb = load_workbook(filename)
        ws = wb['Лист1']

        last_row = ws.max_row
        free_row = last_row + 1
        for col, value in enumerate(data, start=1):
            ws.cell(row=free_row, column=col, value=value)

        for col, value in enumerate(data+[action], start=1):
            ws.cell(row=free_row, column=col, value=value)

        wb.save(filename)
        wb.close()

        return [0,0]
    except Exception as e:
        return [1,e]

print(type(write_excel("fdf",["fdf"], "gfgf")[1]))