import os
import sys

from openpyxl import Workbook

import static_info as stat_inf
import user_info as user_inf
import app_info as app_inf


data_file = "app_info.data"
dir_path = stat_inf.do_not_know
data_path = stat_inf.do_not_know

excel_log = "currents_logs.xlsx"
excel_file = stat_inf.do_not_know

# Узнаем путь, откуда запущена программа и создаем пути
def get_current_dir():
    global dir_path, data_path, excel_file, excel_log
    if getattr(sys, 'frozen', False):
        dir_path = os.path.dirname(os.path.abspath(sys.executable))
    else:
        dir_path = os.path.dirname(os.path.abspath(__file__))

    data_path = os.path.join(dir_path, data_file)
    excel_file = os.path.join(dir_path, excel_log)
    app_inf.local_log_path = excel_file

def check_info_app():
    return os.path.exists(data_path)

def create_info_app():
    with open(data_path, 'w', encoding='utf-8') as f:
        f.write(user_inf.ip_server[0]+"="+'\n')
        f.write(user_inf.file_server[0] + "=" + '\n')
        f.write(user_inf.username[0] + "=" + '\n')


        for i in stat_inf.path_program:
            f.write(i[0] + "=" + '\n')

        f.write(user_inf.ping_global[0] + "=" + '\n')
        f.write(user_inf.ping_local[0] + "=" + '\n')



def write_info_app(field: str, value: str):
    lines = ""
    newlines = ""
    with open(data_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for i in lines:
        i = i.replace("\n","")
        if i.split("=")[0] == field:
            newlines +=field+"="+value+"\n"
        else:
            newlines+=i+"\n"

    with open(data_path, 'w', encoding='utf-8') as f:
        f.write(newlines)


def create_or_replace_excel():
    if os.path.exists(excel_file):
        os.remove(excel_file)

    # Создаём новую книгу и сохраняем
    wb = Workbook()

    sheet = wb.active
    sheet.title = "Лист1"
    ws = wb['Лист1']

    for col, value in enumerate(["Заявка", "Исполнитель", "Текущий кабинет ПК", "Целевой кабинет ПК", "Владелец ПК",
                                 "Подразделение", "Дата", "Действие", "Примечание"], start=1):
        ws.cell(row=1, column=col, value=value)

    wb.save(excel_file)
