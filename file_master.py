import os
import sys
import static_info as stat_inf
import user_info as user_inf


data_file = "app_info.data"
dir_path = stat_inf.do_not_know
data_path = stat_inf.do_not_know

# Узнаем путь, откуда запущена программа и создаем пути
def get_current_dir():
    global dir_path, data_path
    if getattr(sys, 'frozen', False):
        dir_path = os.path.dirname(os.path.abspath(sys.executable))
    else:
        dir_path = os.path.dirname(os.path.abspath(__file__))

    data_path = os.path.join(dir_path, data_file)

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
