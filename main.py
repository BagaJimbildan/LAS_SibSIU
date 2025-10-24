import sys

from PySide6.QtWidgets import QApplication
from design_ui.ui_main_script import MainWindow

import methods.start_info as start_inf


start_inf.check_system()
start_inf.check_domain()
start_inf.check_activate()
start_inf.check_dhcp()
start_inf.check_network()


app = QApplication(sys.argv)
temp = MainWindow()
temp.show()
sys.exit(app.exec())