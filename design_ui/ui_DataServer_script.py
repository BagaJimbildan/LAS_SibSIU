from PySide6.QtWidgets import QDialog
import file_master as file_m
import user_info

from design_ui.ui_DataServer import Ui_DialogDataServer


class DialogDataServer(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogDataServer()
        self.ui.setupUi(self)

        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_ok.clicked.connect(self.save_server)

    def save_server(self):
        file_m.write_info_app(user_info.ip_server[0], self.ui.tb_server.text())
        file_m.write_info_app(user_info.username[0], self.ui.tb_username.text())