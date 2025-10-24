from PySide6.QtWidgets import QDialog

from design_ui.ui_ParamNet import Ui_DialogParamNet

import static_info as stat_inf


class DialogParamNet(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogParamNet()
        self.ui.setupUi(self)

        self.ui.lbl_ip.setText(stat_inf.net_ip_addr)
        self.ui.lbl_mask.setText(stat_inf.net_mask)
        self.ui.lbl_gateway.setText(stat_inf.net_gateway)
        self.ui.lbl_dns1.setText(stat_inf.net_dns[0])
        self.ui.lbl_dns2.setText(stat_inf.net_dns[1])