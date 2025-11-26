from PyQt6.QtWidgets import QPushButton
from PySide6.QtWidgets import QMainWindow

import key_phrases
import static_info as stat_inf
import methods.create_standart as create_standart
from design_ui.ui_ParamNet_script import DialogParamNet
from design_ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow):

    buttons_admin: list[QPushButton]  # кнопки, которые доступны только админу


    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.buttons_admin = \
        [
           self.ui.btn_enable_admin
        ]

        self.ui.lbl_os.setText(stat_inf.platform)
        self.ui.lbl_domen.setText(stat_inf.domain)
        self.ui.lbl_os_activate.setText(stat_inf.activate)
        self.ui.lbl_dhcp.setText(stat_inf.dhcp)
        self.ui.lbl_admin_active.setText(stat_inf.admin_active)

        self.ui.btn_net_1.clicked.connect(self.parameters_net)
        self.ui.btn_enable_admin.clicked.connect(self.enable_admin_param)

        if stat_inf.admin_current_user == 0:
            self.unenable_buttons()
            self.ui.lbl_status_user.setText("Программа запущена НЕ от администратора")
        elif stat_inf.admin_current_user == 1:
            self.ui.lbl_status_user.setText("Программа запущена от администратора")

        # Отключение кнопки "Включить учетную запись админа"
        if stat_inf.admin_active == key_phrases.enabled[1] and self.ui.btn_enable_admin.isEnabled():
            self.ui.btn_enable_admin.setEnabled(False)


    def parameters_net(self):
        self.dialogParamNet = DialogParamNet()
        self.dialogParamNet.show()

    def enable_admin_param(self):
        create_standart.enable_admin(self.ui.lbl_admin_active, self.ui.btn_enable_admin)


    def unenable_buttons(self):
        for i in self.buttons_admin:
            i.setEnabled(False)