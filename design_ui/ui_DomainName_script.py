from PyQt6.QtWidgets import QLabel
from PySide6.QtWidgets import QDialog

from design_ui.ui_DomainName import Ui_DialogDomainName
import methods.create_standart as create_standard
import static_info as stat_inf


class DialogDomainName(QDialog):
    def __init__(self,
                 dialogError,
                 dialogSuccess,
                 lbl_domain: QLabel):  # текущий домен на главном окне
        super().__init__()
        self.ui = Ui_DialogDomainName()
        self.ui.setupUi(self)

        self.dialogError = dialogError
        self.dialogSuccess = dialogSuccess
        self.lbl_domain = lbl_domain

        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_ok.clicked.connect(self.trying_connect)

    def trying_connect(self):

        # Проверка на то, что поля не пустые
        domain = self.ui.tb_domain.text().strip()
        user = self.ui.tb_user.text().strip()
        password = self.ui.tb_pass.text().strip()

        fields = [
            ("домен", domain),
            ("имя пользователя", user),
            ("пароль", password)
        ]

        errors = []
        for field_name, value in fields:
            if create_standard.check_tb_null(value) == 1:
                errors.append(f"Введите {field_name}")

        if errors:
            self.dialogError("\n".join(errors))
        else:
            # Попытка ввода в домен
            status = create_standard.connect_domain(domain, user, password)
            if status[0] == 0:
                self.lbl_domain.setText(domain + " (требуется перезагрузка")
                stat_inf.domain = domain
                self.dialogSuccess("Компьютер введен в домен " + domain+ "\nТребуется перезагрузка компьютера")
                self.close()
            else:
                self.dialogError(status[1])



