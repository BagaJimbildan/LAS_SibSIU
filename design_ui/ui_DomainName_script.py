from PySide6.QtWidgets import QDialog

from design_ui.ui_DomainName import Ui_DialogDomainName


class DialogDomainName(QDialog):
    def __init__(self,
                 error,  # метод вызова окна ошибки
                 success):  # метод вызова окна успеха
        super().__init__()
        self.ui = Ui_DialogDomainName()
        self.ui.setupUi(self)

        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_ok.clicked.connect(self.trying_connect)

    def trying_connect(self):
        pass  # тут пингануть надо и проверить есть ли написанно
