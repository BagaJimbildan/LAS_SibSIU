import user_info as user_inf
import static_info as stat_inf

is_first = True  # первый ли запуск данного экземпляра программы
write_server = False  # записывать ли на сервер

def start_info_app(data_path, change_design):  # чтение информации и смена параметров
    lines = ""
    with open(data_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    k = len(lines)

    user_inf.design_theme[1] = get_value(lines[0])
    user_inf.design_color[1] = get_value(lines[1])

    change_design(user_inf.design_theme[1], user_inf.design_color[1])

    user_inf.ip_server[1] = get_value(lines[2])
    user_inf.file_server[1] = get_value(lines[3])
    user_inf.username[1] = get_value(lines[4])

    n=5  # первые занятые строки

    for i in range(n, k-2):
        path = get_value(lines[i])
        if path != "":
            stat_inf.path_program[i-n][1] = path

    a = get_value(lines[k-2])
    if a != "":
        user_inf.ping_global[1] = a
    a = get_value(lines[k - 1])
    if a != "":
        user_inf.ping_local[1] = a







def get_value(line):
    return line.split("=")[1].replace("\n","")
