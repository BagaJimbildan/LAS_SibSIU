from PySide6.QtWidgets import QDialog
import static_info as stat_inf
import key_phrases as k_phras

from design_ui.ui_LoopFunction import Ui_DialogLoopFunction


class DialogLoopFunction(QDialog):
    def __init__(self,
                 set_time,
                 sync_time,
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
        self.set_time = set_time
        self.sync_time = sync_time
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
        if stat_inf.activate_office == k_phras.activate_status[0]:
            self.ui.cb_office.setEnabled(False)

        if stat_inf.admin_active == k_phras.enabled[1]:
            self.ui.cb_admin.setEnabled(False)

        if stat_inf.hour_zone == k_phras.hour_zone[1] and stat_inf.auto_set_time == k_phras.enabled[1]:
            self.ui.cb_set_time.setEnabled(False)

        if stat_inf.auto_set_time == k_phras.enabled_no[1]:
            self.ui.cb_sync_time.setEnabled(False)

        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_ok.clicked.connect(self.start_loop)

    def start_loop(self):
        if self.ui.cb_set_time.isChecked():
            self.set_time()
        if self.ui.cb_sync_time.isChecked():
            self.sync_time()
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