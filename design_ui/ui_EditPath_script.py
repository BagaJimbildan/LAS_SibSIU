from PySide6.QtWidgets import QDialog, QFileDialog

from design_ui.ui_EditPath import Ui_DialogEditPath
import static_info as stat_inf


class DialogEditPath(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DialogEditPath()
        self.ui.setupUi(self)


        self.ui.btn_ok.clicked.connect(self.close)

        self.ui.btn_driver.clicked.connect(self.path_driver)
        self.ui.btn_of10.clicked.connect(self.path_office2010)
        self.ui.btn_of10A.clicked.connect(self.path_office2010A)
        self.ui.btn_of16.clicked.connect(self.path_office2016)
        self.ui.btn_ar.clicked.connect(self.path_acrobat_reader)
        self.ui.btn_fr.clicked.connect(self.path_fine_reader)
        self.ui.btn_7z.clicked.connect(self.path_7zip)

        self.write_path()


    def path_driver(self):
        result = self.open_explorer()
        if result is not None and result != "":
            stat_inf.path_drivers = result
            self.ui.lbl_path_driver.setText(result)

    def path_office2010(self):
        result = self.open_explorer()
        if result is not None and result != "":
            stat_inf.path_office2010 = result
            self.ui.lbl_path_of10.setText(result)

    def path_office2010A(self):
        result = self.open_explorer()
        if result is not None and result != "":
            stat_inf.path_office2010A = result
            self.ui.lbl_path_of10A.setText(result)

    def path_office2016(self):
        result = self.open_explorer()
        if result is not None and result != "":
            stat_inf.path_office2016 = result
            self.ui.lbl_path_of16.setText(result)

    def path_acrobat_reader(self):
        result = self.open_explorer()
        if result is not None and result != "":
            stat_inf.path_AcrobatReader = result
            self.ui.lbl_path_ar.setText(result)

    def path_fine_reader(self):
        result = self.open_explorer()
        if result is not None and result != "":
            stat_inf.path_fineReader = result
            self.ui.lbl_path_fr.setText(result)

    def path_7zip(self):
        result = self.open_explorer()
        if result is not None and result != "":
            stat_inf.path_7zip = result
            self.ui.lbl_path_7z.setText(result)

    def open_explorer(self):
        self.file_path = QFileDialog.getOpenFileName(
            None,  # родительское окно
            "Выберите файл",  # заголовок окна
            "",  # начальная директория (пустая - последняя использованная)
            "Программы (*.exe)"  # фильтры
        )
        return self.file_path[0]

    def write_path(self):
        self.ui.lbl_path_driver.setText(stat_inf.path_drivers)

        self.ui.lbl_path_of10.setText(stat_inf.path_office2010)
        self.ui.lbl_path_of10A.setText(stat_inf.path_office2010A)
        self.ui.lbl_path_of16.setText(stat_inf.path_office2016)
        self.ui.lbl_path_fr.setText(stat_inf.path_fineReader)
        self.ui.lbl_path_ar.setText(stat_inf.path_AcrobatReader)
        self.ui.lbl_path_7z.setText(stat_inf.path_7zip)