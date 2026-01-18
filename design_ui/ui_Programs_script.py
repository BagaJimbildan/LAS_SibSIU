from PySide6.QtWidgets import QDialog

from design_ui.ui_Programs import Ui_DialogPrograms


class DialogPrograms(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogPrograms()
        self.ui.setupUi(self)