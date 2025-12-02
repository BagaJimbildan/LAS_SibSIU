from PyQt6.QtWidgets import QPushButton
from PySide6.QtWidgets import QMainWindow

import key_phrases
import static_info as stat_inf
import methods.create_standart as create_standard
from design_ui.ui_CreatePass_script import DialogCreatePass
from design_ui.ui_EditNetwork_script import DialogEditNetwork
from design_ui.ui_Error_script import DialogError
from design_ui.ui_ParamNet_script import DialogParamNet
from design_ui.ui_StandardName_script import DialogStandardName
from design_ui.ui_Success_script import DialogSuccess
from design_ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow):

    buttons_admin: list[QPushButton]  # кнопки, которые доступны только админу


    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.buttons_admin = \
        [
            self.ui.btn_enable_admin,
            self.ui.btn_pass_admin,
            self.ui.btn_edit_name
        ]

        self.ui.lbl_os.setText(stat_inf.platform)
        self.ui.lbl_domen.setText(stat_inf.domain)
        self.ui.lbl_os_activate.setText(stat_inf.activate)
        self.ui.lbl_dhcp.setText(stat_inf.dhcp)
        self.ui.lbl_admin_active.setText(stat_inf.admin_active)
        self.ui.lbl_name.setText(stat_inf.name_PC)
        self.ui.lbl_name_is_standart.setText(stat_inf.name_PC_standard)

        self.ui.btn_net_1.clicked.connect(self.parameters_net)
        self.ui.btn_enable_admin.clicked.connect(self.enable_admin_param)
        self.ui.btn_pass_admin.clicked.connect(self.open_window_password)
        self.ui.btn_edit_name.clicked.connect(self.dialog_edit_name_show)
        self.ui.btn_edit_network.clicked.connect(self.dialog_edit_network_show)

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
        status = create_standard.enable_admin(self.ui.lbl_admin_active, self.ui.btn_enable_admin)

        if status[0] == 1:
            self.dialog_error_show(status[1])
        else:
            self.dialog_success_show("Учетная запись администратора успешно включена")

    def unenable_buttons(self):
        for i in self.buttons_admin:
            i.setEnabled(False)

    def open_window_password(self):
        self.dialogPassAdmin = DialogCreatePass()
        self.dialogPassAdmin.ui.btn_ok.clicked.connect(self.start_change_pass)
        self.dialogPassAdmin.setWindowTitle("Задать пароль администратора")
        self.dialogPassAdmin.ui.lb_info.setText("Введите и подтвердите пароль встроенной учетной записи администратора")
        self.dialogPassAdmin.show()

    def start_change_pass(self):
        pass1 = self.dialogPassAdmin.ui.tb_pass1.text()
        pass2 = self.dialogPassAdmin.ui.tb_pass2.text()

        if pass1 == pass2:
            status = create_standard.pass_admin(pass1)
            if status[0] == 1:
                self.dialog_error_show(status[1])
            else:
                self.dialog_success_show("Пароль администратора успешно изменен")
                self.dialogPassAdmin.close()

        else:
            self.dialog_error_show("Введеные пароли не совпадают")

    def dialog_error_show(self, text: str):
        self.dialogError = DialogError()
        self.dialogError.ui.tb_error.setText(text)
        self.dialogError.show()

    def dialog_success_show(self, text: str):
        self.dialogSuccess = DialogSuccess()
        self.dialogSuccess.ui.tb_info.setText(text)
        self.dialogSuccess.show()

    def dialog_edit_name_show(self):
        self.dialogEditName = DialogStandardName(self.ui.lbl_name, self.ui.lbl_name_is_standart, self.dialog_success_show, self.dialog_error_show)
        self.dialogEditName.show()

    def dialog_edit_network_show(self):
        self.dialogEditNetwork = DialogEditNetwork(self.dialog_error_show, self.dialog_success_show)
        self.dialogEditNetwork.show()