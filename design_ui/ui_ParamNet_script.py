from PySide6.QtWidgets import QDialog

from design_ui.ui_ParamNet import Ui_DialogParamNet


class DialogParamNet(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogParamNet()
        self.ui.setupUi(self)