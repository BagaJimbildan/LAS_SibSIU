from PySide6.QtWidgets import QDialog

from design_ui.ui_DataServer import Ui_DialogDataServer


class DialogDataServer(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogDataServer()
        self.ui.setupUi(self)

        self.ui.btn_cancel.clicked.connect(self.close)