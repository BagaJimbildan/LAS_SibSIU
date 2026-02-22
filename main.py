import os
import subprocess
import sys

from PySide6.QtWidgets import QApplication
from design_ui.ui_main_script import MainWindow

import methods.start_info as start_inf
import file_master as file_m
import app_info as app_inf
import server_setting as serv_set


start_inf.check_system()
start_inf.check_domain()
start_inf.check_activate()
start_inf.check_name()
start_inf.check_name_standard()
start_inf.check_dhcp()
start_inf.check_network()
start_inf.check_admin_on()

start_inf.check_status_current_user()

file_m.get_current_dir()  # определение директории программы

if file_m.check_info_app():  # если есть файл с информацией о данном экземпляре программы
    app_inf.is_first = False
    app_inf.start_info_app(file_m.data_path)  # определение информации о данном экземпляре программы
else:
    app_inf.is_first = True
    file_m.create_info_app()  # создание файла с информацией

def cleanup():
    if app_inf.write_server:
        serv_set.disconnect_server()

app = QApplication(sys.argv)
app.aboutToQuit.connect(cleanup)
temp = MainWindow()
temp.show()
sys.exit(app.exec())
