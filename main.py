import platform
import sys

from PySide6.QtWidgets import QApplication

import static_info as s_info
from design_ui.ui_main_script import MainWindow

os_version = platform.platform()
s_info.os = platform.system()
s_info.platform = platform.platform()

app = QApplication(sys.argv)
temp = MainWindow()
temp.show()
sys.exit(app.exec())