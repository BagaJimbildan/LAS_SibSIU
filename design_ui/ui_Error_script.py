from PySide6.QtWidgets import QDialog

from design_ui.ui_Error import Ui_DialogError


class DialogError(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogError()
        self.ui.setupUi(self)

        self.ui.btn_close.clicked.connect(self.close)