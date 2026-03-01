from PyQt6.QtWidgets import QLabel
from PySide6.QtWidgets import QDialog
import file_master as file_m
import user_info as user_inf
import static_info as stat_inf

from design_ui.ui_EditPing import Ui_DialogEditPing


class DialogEditPing(QDialog):
    def __init__(self, local, lbl_name: QLabel, lbl_time: QLabel, lbl_status: QLabel):
        super().__init__()
        self.ui = Ui_DialogEditPing()
        self.ui.setupUi(self)

        self.local = local

        self.lbl_name = lbl_name
        self.lbl_time = lbl_time
        self.lbl_status = lbl_status

        self.ui.tb_hostname.setText(user_inf.ping_local[1] if local else user_inf.ping_global[1])

        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_save.clicked.connect(self.save_hosts)
        # Сделать проверку записи и кнопку сохранить и проверить, а потом еще закрыть надо


    def save_hosts(self):
        if self.local:
            user_inf.ping_local[1] = self.ui.tb_hostname.text().strip()
            file_m.write_info_app(user_inf.ping_local[0], user_inf.ping_local[1])
        else:
            user_inf.ping_global[1] = self.ui.tb_hostname.text().strip()
            file_m.write_info_app(user_inf.ping_global[0], user_inf.ping_global[1])

        self.lbl_name.setText(self.ui.tb_hostname.text().strip())
        self.lbl_status.setText(stat_inf.default_note)
        self.lbl_time.setText(stat_inf.default_note)

