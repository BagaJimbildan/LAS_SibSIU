from PySide6.QtWidgets import QDialog
import static_info as stat_inf
import key_phrases as k_phras

from design_ui.ui_LoopFunction import Ui_DialogLoopFunction


class DialogLoopFunction(QDialog):
    def __init__(self,
                 admin_activate,
                 admin_pass,
                 start_admin_disable,
                 activate_os,
                 activate_office,
                 change_name,
                 domain,
                 edit_network):
        super().__init__()
        self.ui = Ui_DialogLoopFunction()
        self.ui.setupUi(self)

        # список функции
        self.admin_active = admin_activate
        self.admin_pass = admin_pass
        self.start_admin_disable = start_admin_disable
        self.activate_os = activate_os
        self.activate_office = activate_office
        self.change_name = change_name
        self.domain = domain
        self.edit_network = edit_network


        if stat_inf.activate == k_phras.activate_status[0]:
            self.ui.cb_windows.setEnabled(False)

        if stat_inf.admin_active == k_phras.enabled[1]:
            self.ui.cb_admin.setEnabled(False)

        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_ok.clicked.connect(self.start_loop)

    def start_loop(self):
        if self.ui.cb_admin.isChecked():
            self.admin_active()
        if self.ui.cb_pass_admin.isChecked():
            self.admin_pass()
        if self.ui.cb_user.isChecked():
            self.start_admin_disable()
        if self.ui.cb_windows.isChecked():
            self.activate_os()
        if self.ui.cb_office.isChecked():
            self.activate_office()
        if self.ui.cb_name_pc.isChecked():
            self.change_name()
        if self.ui.cb_domain.isChecked():
            self.domain()
        if self.ui.cb_network.isChecked():
            self.edit_network()
        self.close()