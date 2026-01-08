from PySide6.QtWidgets import QDialog

from design_ui.ui_DisableUser import Ui_DialogDisableUser

import methods.create_standart as create_standard

class DialogDisableUser(QDialog):
    def __init__(self, dialogError, dialogSuccess):
        super().__init__()
        self.ui = Ui_DialogDisableUser()
        self.ui.setupUi(self)

        self.ui.tb_name.setText("user")

        self.dialogError = dialogError
        self.dialogSuccess = dialogSuccess
        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_ok.clicked.connect(self.check_name)

    def check_name(self):
        name = self.ui.tb_name.text()

        if name is None or name.strip() == "":
            self.dialogError("Введите имя пользователя администратора")
        else:
            status = create_standard.disable_user(name)
            if status[0] == 1:
                self.dialogError(status[1])
            else:
                self.dialogSuccess("Учетная запись "+ name+ " успешно отключена")
