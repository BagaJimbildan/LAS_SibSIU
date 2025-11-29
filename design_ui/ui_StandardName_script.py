import re

from PySide6.QtWidgets import QDialog

from design_ui.ui_StandardName import Ui_DialogStandardName


class DialogStandardName(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogStandardName()
        self.ui.setupUi(self)

        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_ok.clicked.connect(self.start_edit_name)

        self.ui.cb_type.addItem("компьютер", "С")
        self.ui.cb_type.addItem("ноутбук", "N")
        self.ui.cb_type.addItem("интерактивная панель", "P")

    def start_edit_name(self):
        print(self.check_num_cab_text())

    def check_num_cab_text(self):
        text = self.ui.tb_num_cab.text().strip()

        if text is None or text == "":
            return [1, "необходимо заполнить"]

        if len(text) > 10:
            return [1, "не должно быть более 10 символов"]

        pattern = r'^[a-zA-Z0-9]*$'
        if not bool(re.match(pattern, text)):
            return [1, "допустимы только латинские буквы и цифры"]

        return [0,0]

    def check_num_inv_text(self):
        text = self.ui.tb_num_inv.text().strip()

        if text is None or text == "":
            return [1, "необходимо заполнить"]

        pattern = r'^\d{5}$'
        if not bool(re.match(pattern, text)):
            return [1, "должно быть ровно 5 цифр"]

        return [0, 0]

