from PySide6.QtWidgets import QMainWindow

import static_info
from design_ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # в зависимости от того какая ос смотрим активацию
        self.ui.lbl_os.setText(static_info.platform)