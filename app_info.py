import user_info as user_inf
import static_info as stat_inf

is_first = True  # первый ли запуск данного экземпляра программы
write_server = False  # записывать ли на сервер

def start_info_app(data_path):  # чтение информации и смена параметров
    lines = ""
    with open(data_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    k = len(lines)

    user_inf.ip_server[1] = get_value(lines[0])
    user_inf.file_server[1] = get_value(lines[1])
    user_inf.username[1] = get_value(lines[2])

    for i in range(3, k-2):
        path = get_value(lines[i])
        if path != "":
            stat_inf.path_program[i-3][1] = path


    user_inf.ping_global[1] = get_value(lines[k-2])
    user_inf.ping_local[1] = get_value(lines[k-1])






def get_value(line):
    return line.split("=")[1].replace("\n","")
