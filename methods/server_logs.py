from openpyxl import load_workbook

path_log = None

def write_excel(data:list[str], action: str):
    try:
        if path_log is not None:
            excel = load_workbook(path_log)
            wb = load_workbook(path_log)
            ws = wb['Лист1']

            last_row = ws.max_row
            free_row = last_row + 1
            for col, value in enumerate(data, start=1):
                ws.cell(row=free_row, column=col, value=value)

            for col, value in enumerate(data+[action], start=1):
                ws.cell(row=free_row, column=col, value=value)

            wb.save(path_log)
            wb.close()

            # еще дату записывать бы
        else:
            return [1, "Сервер отключен или файл не найден"]
        return [0,0]
    except Exception as e:
        return [1,e]
