from PySide6.QtWidgets import QDialog

from design_ui.ui_WriteServer import Ui_DialogWriteServer
import app_info as app_inf
import file_master as file_m


class DialogWriteServer(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogWriteServer()
        self.ui.setupUi(self)

        self.ui.btn_yes.clicked.connect(self.btn_yes)
        self.ui.btn_no.clicked.connect(self.btn_no)

    def btn_yes(self):
        app_inf.write_server = True
        self.not_ask(True)
        self.close()

    def btn_no(self):
        app_inf.write_server = False
        self.not_ask(False)
        self.close()

    def not_ask(self, yes: bool):
        file_m.write_info_app("not_ask_write_server", str(self.ui.cb_asking.isChecked()))
        file_m.write_info_app("write_server_default", str(yes))