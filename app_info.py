import user_info as user_inf
import static_info as stat_inf

is_first = True  # первый ли запуск данного экземпляра программы
write_server = False  # записывать ли на сервер

def start_info_app(data_path):  # чтение информации и смена параметров
    lines = ""
    with open(data_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    user_inf.ip_server[1] = get_value(lines[0])
    user_inf.username[1] = get_value(lines[1])

    for i in range(2, len(lines)):
        path = get_value(lines[i])
        if path != "":
            stat_inf.path_program[i-2][1] = path






def get_value(line):
    return line.split("=")[1].replace("\n","")
