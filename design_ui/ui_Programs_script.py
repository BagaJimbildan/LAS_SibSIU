from PySide6.QtWidgets import QDialog
import static_info as stat_inf

from design_ui.ui_Programs import Ui_DialogPrograms
import methods.program_setup as prog_set


class DialogPrograms(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_DialogPrograms()
        self.ui.setupUi(self)
        self.parent = parent

        self.ui.btn_ok.clicked.connect(self.close)

        self.ui.btn_of10.clicked.connect(self.setup_office2010)
        self.ui.btn_of10A.clicked.connect(self.setup_office2010A)
        self.ui.btn_of16.clicked.connect(self.setup_office2016)
        self.ui.btn_ar.clicked.connect(self.setup_acrobat_reader)
        self.ui.btn_fr.clicked.connect(self.setup_fine_reader)
        self.ui.btn_7z.clicked.connect(self.setup_7zip)

    def setup_office2010(self):
        prog_set.setup_program(self.parent, "Установщик Office 2010", stat_inf.path_office2010)

    def setup_office2010A(self):
        prog_set.setup_program(self.parent, "Установщик Office 2010 с Access", stat_inf.path_office2010A)

    def setup_office2016(self):
        prog_set.setup_program(self.parent, "Установщик Office 2016", stat_inf.path_office2016)

    def setup_acrobat_reader(self):
        prog_set.setup_program(self.parent, "Установщик Acrobat Reader", stat_inf.path_AcrobatReader)

    def setup_fine_reader(self):
        prog_set.setup_program(self.parent, "Установщик ABBYY FineReader", stat_inf.path_fineReader)

    def setup_7zip(self):
        prog_set.setup_program(self.parent, "Установщик 7zip", stat_inf.path_7zip)

