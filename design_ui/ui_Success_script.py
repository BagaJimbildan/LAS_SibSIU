from PySide6.QtWidgets import QDialog

from design_ui.ui_Success import Ui_DialogSuccess


class DialogSuccess(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogSuccess()
        self.ui.setupUi(self)

        self.ui.btn_close.clicked.connect(self.close)