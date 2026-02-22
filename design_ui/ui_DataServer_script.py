import subprocess

from PySide6.QtWidgets import QDialog
import file_master as file_m
import user_info as user_inf

from design_ui.ui_DataServer import Ui_DialogDataServer
import methods.create_standart as create_standard


class DialogDataServer(QDialog):
    def __init__(self,dialogError, dialogSuccess):
        super().__init__()
        self.ui = Ui_DialogDataServer()
        self.ui.setupUi(self)

        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_ok.clicked.connect(self.try_connect)

        self.dialogError = dialogError
        self.dialogSuccess = dialogSuccess

    def save_server(self):
        file_m.write_info_app(user_inf.ip_server[0], self.ui.tb_server.text())
        file_m.write_info_app(user_inf.username[0], self.ui.tb_username.text())
        file_m.write_info_app(user_inf.file_server[0], self.ui.tb_file_server.text())

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
            ("сервер", server),
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
