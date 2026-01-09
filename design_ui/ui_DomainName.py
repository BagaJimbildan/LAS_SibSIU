# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DomainName.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_DialogDomainName(object):
    def setupUi(self, DialogDomainName):
        if not DialogDomainName.objectName():
            DialogDomainName.setObjectName(u"DialogDomainName")
        DialogDomainName.resize(397, 193)
        self.btn_ok = QPushButton(DialogDomainName)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(280, 160, 101, 26))
        self.btn_cancel = QPushButton(DialogDomainName)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(190, 160, 81, 26))
        self.tb_domain = QLineEdit(DialogDomainName)
        self.tb_domain.setObjectName(u"tb_domain")
        self.tb_domain.setGeometry(QRect(180, 40, 201, 31))
        self.tb_pass = QLineEdit(DialogDomainName)
        self.tb_pass.setObjectName(u"tb_pass")
        self.tb_pass.setGeometry(QRect(180, 120, 201, 31))
        self.tb_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.label = QLabel(DialogDomainName)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 90, 41, 16))
        self.label_2 = QLabel(DialogDomainName)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 130, 41, 16))
        self.tb_user = QLineEdit(DialogDomainName)
        self.tb_user.setObjectName(u"tb_user")
        self.tb_user.setGeometry(QRect(180, 80, 201, 31))
        self.lbl_domain = QLabel(DialogDomainName)
        self.lbl_domain.setObjectName(u"lbl_domain")
        self.lbl_domain.setGeometry(QRect(120, 50, 51, 16))
        self.label_3 = QLabel(DialogDomainName)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 10, 361, 16))

        self.retranslateUi(DialogDomainName)

        QMetaObject.connectSlotsByName(DialogDomainName)
    # setupUi

    def retranslateUi(self, DialogDomainName):
        DialogDomainName.setWindowTitle(QCoreApplication.translate("DialogDomainName", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u0434\u043e\u043c\u0435\u043d\u0430", None))
        self.btn_ok.setText(QCoreApplication.translate("DialogDomainName", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u0441\u044f", None))
        self.btn_cancel.setText(QCoreApplication.translate("DialogDomainName", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.label.setText(QCoreApplication.translate("DialogDomainName", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_2.setText(QCoreApplication.translate("DialogDomainName", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.lbl_domain.setText(QCoreApplication.translate("DialogDomainName", u"\u0414\u043e\u043c\u0435\u043d:", None))
        self.label_3.setText(QCoreApplication.translate("DialogDomainName", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0443\u0447\u0435\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f \u0441 \u043f\u0440\u0430\u0432\u043e\u043c \u0432\u0432\u043e\u0434\u0430 \u0432 \u0434\u043e\u043c\u0435\u043d", None))
    # retranslateUi

