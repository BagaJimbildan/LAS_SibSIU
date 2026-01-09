from PyQt6.QtWidgets import QLineEdit
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QDialog

import methods.create_standart as create_standard
from design_ui.ui_EditNetwork import Ui_DialogEditNetwork
import static_info as stat_inf


class DialogEditNetwork(QDialog):
    def __init__(self,
                 error,  # метод вызова окна ошибки
                 success):  # метод вызова окна успеха
        super().__init__()
        self.ui = Ui_DialogEditNetwork()
        self.ui.setupUi(self)

        self.error = error
        self.success = success
        validator = QIntValidator(0, 255)
        self.set_standart_tb(self.ui.tb_ip1, validator)
        self.set_standart_tb(self.ui.tb_ip2, validator)
        self.set_standart_tb(self.ui.tb_ip3, validator)
        self.set_standart_tb(self.ui.tb_ip4, validator)

        self.ui.tb_ip1.textChanged.connect(self.ip1_cnange)
        self.ui.tb_ip2.textChanged.connect(self.ip2_cnange)
        self.ui.tb_ip3.textChanged.connect(self.ip3_cnange)
        self.ui.tb_ip4.textChanged.connect(self.ip4_cnange)

        self.ui.btn_ok.clicked.connect(self.start_edit_network)
        self.ui.btn_cancel.clicked.connect(self.close)

    def set_standart_tb(self, tb:QLineEdit, validator: QIntValidator):
        tb.setValidator(validator)
        tb.setPlaceholderText("0-255")

    def ip_changed(self, text:str, tb:QLineEdit):
        tb.setText(text.replace(" ", ""))
        if text.strip() != "" and int(text) > 255:
            tb.setText("255")

    def ip1_cnange(self, text):
        self.ip_changed(text, self.ui.tb_ip1)
    def ip2_cnange(self, text):
        self.ip_changed(text, self.ui.tb_ip2)
    def ip3_cnange(self, text):
        self.ip_changed(text, self.ui.tb_ip3)
    def ip4_cnange(self, text):
        self.ip_changed(text, self.ui.tb_ip4)

    def start_edit_network(self):
        if (self.ui.tb_ip1.text().strip() == "" or
            self.ui.tb_ip2.text().strip() == "" or
            self.ui.tb_ip3.text().strip() == "" or
            self.ui.tb_ip4.text().strip() == ""):
                self.error("Введите корректный ip адрес")
        else:
            ip = [self.ui.tb_ip1.text().strip(), self.ui.tb_ip2.text().strip(),
                  self.ui.tb_ip3.text().strip(), self.ui.tb_ip4.text().strip()]
            status = create_standard.edit_network(ip)
            if status[0] == 1:
                self.error(status[1])
            else:
                text = "Параметры сети успешно изменены:\n"
                text += f"ip: {".".join(ip)}\n"
                text += f"шлюз: {".".join(ip[0:-1]) + ".254"}\n"
                text += f"маска: 255.255.255.0\n"
                text += "DNS: 10.252.253.1, 10.252.253.2"

                stat_inf.net_ip_addr = f"{".".join(ip)}"
                stat_inf.net_gateway = f"{".".join(ip[0:-1]) + ".254"}"
                stat_inf.net_mask = "255.255.255.0"
                stat_inf.net_dns = ["10.252.253.1", "10.252.253.2"]
                self.success(text)
                self.close()



