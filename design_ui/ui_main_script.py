from PySide6.QtWidgets import QMainWindow

import static_info as stat_inf
from design_ui.ui_ParamNet_script import DialogParamNet
from design_ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # в зависимости от того какая ос смотрим активацию
        self.ui.lbl_os.setText(stat_inf.platform)
        self.ui.lbl_domen.setText(stat_inf.domain)
        self.ui.lbl_os_activate.setText(stat_inf.activate)
        self.ui.lbl_dhcp.setText(stat_inf.dhcp)
        self.ui.lbl_admin_active.setText(stat_inf.admin_active)

        self.ui.btn_net_1.clicked.connect(self.parameters_net)

    def parameters_net(self):
        self.dialogParamNet = DialogParamNet()
        self.dialogParamNet.show()