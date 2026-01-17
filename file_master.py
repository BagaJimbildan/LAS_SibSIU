import os
import sys
import static_info as stat_inf


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
    with open(data_path, 'w', encoding='utf-8'):
        pass


def read_info_app():
    pass

def write_info_app(field: str, value: str):
    print(field, value)

    with open(data_path, 'a', encoding='utf-8') as f:
        f.write(field+"="+value+"\n")
