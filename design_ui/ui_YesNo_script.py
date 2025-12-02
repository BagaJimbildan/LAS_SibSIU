from PySide6.QtWidgets import QDialog

from design_ui.ui_YesNo import Ui_DialogYesNo


class DialogYesNo(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogYesNo()
        self.ui.setupUi(self)

        self.ui.btn_close.clicked.connect(self.close)