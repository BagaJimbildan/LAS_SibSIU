import os
import subprocess
import sys

from PySide6.QtWidgets import QApplication
from design_ui.ui_main_script import MainWindow
from qt_material import apply_stylesheet

import methods.start_info as start_inf
import create_design.name_themes as name_themes
import file_master as file_m
import app_info as app_inf
import server_setting as serv_set
import user_info as user_inf


start_inf.check_system()
start_inf.check_domain()
start_inf.check_activate()
start_inf.check_name()
start_inf.check_name_standard()
start_inf.check_dhcp()
start_inf.check_network()
start_inf.check_admin_on()
start_inf.check_activate_office()

start_inf.check_status_current_user()


file_m.get_current_dir()  # определение директории программы

app = QApplication(sys.argv)

change_design = lambda theme,color: apply_stylesheet(app, f"{theme}_{color}.xml")

if file_m.check_info_app():  # если есть файл с информацией о данном экземпляре программы
    app_inf.is_first = False
    app_inf.start_info_app(file_m.data_path, change_design)  # определение информации о данном экземпляре программы
else:
    app_inf.is_first = True
    def_theme, def_color = name_themes.th_dark, name_themes.c_teal  # стандартная тема и цвет
    file_m.create_info_app(def_theme, def_color)  # создание файла с информацией, в параметрах стандартная тема, цвет
    user_inf.design_theme[1] = def_theme
    user_inf.design_color[1] = def_color
    change_design(def_theme, def_color)

# Создание файлы логов текущей сессии
file_m.create_or_replace_excel()

def cleanup():
    if app_inf.write_server:
        serv_set.disconnect_server()


app.aboutToQuit.connect(cleanup)
temp = MainWindow(change_design)
temp.show()
sys.exit(app.exec())
