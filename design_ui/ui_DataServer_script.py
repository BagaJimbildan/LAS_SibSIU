import subprocess
from pathlib import Path

from PyQt6.QtGui import QAction
from PySide6.QtWidgets import QDialog
import file_master as file_m
import user_info as user_inf
import app_info as app_inf
import server_setting as serv_set

from design_ui.ui_DataServer import Ui_DialogDataServer
import methods.create_standart as create_standard


class DialogDataServer(QDialog):
    def __init__(self,dialogError, dialogSuccess, button_connect_disconnect: QAction = None):
        super().__init__()
        self.ui = Ui_DialogDataServer()
        self.ui.setupUi(self)

        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_ok.clicked.connect(self.try_connect)

        self.ui.tb_server.setText(user_inf.ip_server[1])
        self.ui.tb_username.setText(user_inf.username[1])
        self.ui.tb_file_server.setText(user_inf.file_server[1])

        self.button_connect_disconnect = button_connect_disconnect

        self.dialogError = dialogError
        self.dialogSuccess = dialogSuccess

    def save_server(self):
        file_m.write_info_app(user_inf.ip_server[0], self.ui.tb_server.text().strip())
        file_m.write_info_app(user_inf.username[0], self.ui.tb_username.text().strip())
        file_m.write_info_app(user_inf.file_server[0], self.ui.tb_file_server.text().strip())

    def write_user_info(self):
        user_inf.ip_server[1] = self.ui.tb_server.text().strip()
        user_inf.username[1] = self.ui.tb_username.text().strip()
        user_inf.file_server[1] = self.ui.tb_file_server.text().strip()

        user_inf.ticket = self.ui.tb_ticket.text().strip()
        user_inf.owner = self.ui.tb_owner.text().strip()
        user_inf.current_room = self.ui.tb_current_room.text().strip()
        user_inf.room = self.ui.tb_room.text().strip()
        user_inf.subdivision = self.ui.tb_subdivision.text().strip()


    def mount_share_windows(self, drive_letter, share_path, username, password):
        cmd = f'net use {drive_letter}: {share_path} /user:{username} {password} /persistent:no'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='cp866')
        if result.returncode == 0:
            return [0,0]
        else:
            return [1, result.stderr]

    def try_connect(self):
        # Проверка на то, что поля не пустые
        server = self.ui.tb_server.text().strip()
        file_server = self.ui.tb_file_server.text().strip()
        username = self.ui.tb_username.text().strip()
        password = self.ui.tb_pass.text().strip()

        fields = [
            ("сетевая папка", server),
            ("файл на сервере", file_server),
            ("имя пользователя", username),
            ("пароль", password)
        ]

        errors = []
        for field_name, value in fields:
            if create_standard.check_tb_null(value) == 1:
                errors.append(f"Введите {field_name}")

        if errors:
            self.dialogError("\n".join(errors))
        else:
            status1 = self.mount_share_windows("Z", server, username, password)
            if status1[0] == 1:
                self.dialogError(status1[1])
                return

            file_server_path = Path("Z:/"+file_server)
            extension = file_server_path.suffix.lower()

            if file_server_path.exists() and file_server_path.is_file():
                if extension in ('.xls', '.xlsx', '.xlsm', '.xlsb'):
                    app_inf.write_server = True

                    # Сохранить при успехе
                    self.save_server()

                    # Записать в текущие данные о подключении
                    self.write_user_info()

                    if self.button_connect_disconnect is not None:
                        self.button_connect_disconnect.setText("Отключиться")

                    self.close()

                else:
                    self.dialogError("Тип файла должен быть электронной таблицей" + "\n"+
                                     "доступные типы: "+"\n"+
                                     "(.xls', '.xlsx', '.xlsm', '.xlsb)")
                    serv_set.disconnect_server()
            else:
                self.dialogError("Файл не найден")
                serv_set.disconnect_server()


