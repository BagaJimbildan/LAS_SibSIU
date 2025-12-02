import re

from PyQt6.QtWidgets import QLabel
from PySide6.QtWidgets import QDialog

import static_info as stat_inf
import key_phrases as k_phras

import methods.create_standart as create_standard
from design_ui.ui_Error_script import DialogError
from design_ui.ui_StandardName import Ui_DialogStandardName
from design_ui.ui_YesNo_script import DialogYesNo


class DialogStandardName(QDialog):
    def __init__(self,
                 label_name: QLabel,  # label для отображения имени в окне
                 label_standard: QLabel, # label для отображения соответствия стандарта имени
                 message_box,  # метод вызова окна для отображения информации
                 error_box):  # метод вызова окна для отображения ошибки
        super().__init__()
        self.ui = Ui_DialogStandardName()
        self.ui.setupUi(self)

        self.label_name = label_name
        self.label_standard = label_standard
        self.message_box = message_box
        self.error_box = error_box

        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_ok.clicked.connect(self.check_rename_name)

        self.ui.tb_num_cab.textChanged.connect(self.write_error_num_cab)
        self.ui.tb_num_inv.textChanged.connect(self.write_error_num_inv)

        self.ui.cb_type.addItem("компьютер", "C")
        self.ui.cb_type.addItem("ноутбук", "N")
        self.ui.cb_type.addItem("интерактивная панель", "P")

        self.new_name = ""

    def check_rename_name(self):
        test1 = self.check_num_cab_text()
        test2 = self.check_num_inv_text()

        # перед этим окно, точно ли хотим поменять
        if test1[0] == 0 and test2[0] == 0:
            self.dialog_yesno = DialogYesNo()

            self.new_name = f"{self.ui.tb_num_cab.text().strip()}-{self.ui.tb_num_inv.text().strip()}-{self.ui.cb_type.currentData()}"
            text = f"Итоговое имя: \n {self.new_name}"

            self.dialog_yesno.ui.btn_ok.clicked.connect(self.start_rename)
            self.dialog_yesno.ui.tb_text.setText(text)

            self.dialog_yesno.show()
        else:
            self.dialogError = DialogError()

            errors = []
            if test1[0] == 1:
                errors.append(f"-Номер кабинета: {test1[1]}")
            if test2[0] == 1:
                errors.append(f"-Инв. номер (5 цифр): {test2[1]}")

            if errors:
                error_word = "ую ошибку" if len(errors) == 1 else "ие ошибки"
                error_text = f"Исправьте следующ{error_word}:\n" + "\n".join(errors)
                self.dialogError.ui.tb_error.setText(error_text)

            self.dialogError.show()



    def write_error_num_cab(self):
        test_error = self.check_num_cab_text()
        if test_error[0] == 1:
            self.ui.lbl_error_num_cab.setText(test_error[1])
        else:
            self.ui.lbl_error_num_cab.setText("")

    def write_error_num_inv(self):
        test_error = self.check_num_inv_text()
        if test_error[0] == 1:
            self.ui.lbl_error_num_inv.setText(test_error[1])
        else:
            self.ui.lbl_error_num_inv.setText("")

    def check_num_cab_text(self):
        text = self.ui.tb_num_cab.text().strip()

        if text is None or text == "":
            return [1, "необходимо заполнить"]

        if len(text) > 10:
            return [1, "не должно быть более 10 символов"]

        pattern = r'^[a-zA-Z0-9]*$'
        if not bool(re.match(pattern, text)):
            return [1, "допустимы только латинские буквы и цифры"]

        return [0,0]

    def check_num_inv_text(self):
        text = self.ui.tb_num_inv.text().strip()

        if text is None or text == "":
            return [1, "необходимо заполнить"]

        pattern = r'^\d{5}$'
        if not bool(re.match(pattern, text)):
            return [1, "должно быть ровно 5 цифр"]

        return [0, 0]

    def start_rename(self):
        status = create_standard.rename_PC(self.new_name)
        if status[0] == 0:
            self.label_name.setText(self.new_name + " (требуется перезагрузка)")
            stat_inf.name_PC = self.new_name
            stat_inf.name_PC_standard = k_phras.matching_yes[0]
            self.label_standard.setText(stat_inf.name_PC_standard)
            text = "Имя компьютера изменено на " + self.new_name + "\n"
            text += f"Требуется перезагрузка для применения изменений"
            self.message_box(text)
            self.dialog_yesno.close()
            self.close()
        else:
            self.error_box(status[1])

