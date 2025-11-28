from PyQt6.QtWidgets import QLineEdit, QCheckBox
from PySide6.QtWidgets import QDialog

from design_ui.ui_CreatePass import Ui_DialogCreatePass


class DialogCreatePass(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogCreatePass()
        self.ui.setupUi(self)

        self.ui.btn_cancel.clicked.connect(self.close)
