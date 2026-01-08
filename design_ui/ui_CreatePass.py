# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreatePass.ui'
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

class Ui_DialogCreatePass(object):
    def setupUi(self, DialogCreatePass):
        if not DialogCreatePass.objectName():
            DialogCreatePass.setObjectName(u"DialogCreatePass")
        DialogCreatePass.resize(464, 134)
        self.lb_info = QLabel(DialogCreatePass)
        self.lb_info.setObjectName(u"lb_info")
        self.lb_info.setGeometry(QRect(20, 10, 441, 16))
        self.lb_info_2 = QLabel(DialogCreatePass)
        self.lb_info_2.setObjectName(u"lb_info_2")
        self.lb_info_2.setGeometry(QRect(20, 40, 131, 16))
        self.lb_info_3 = QLabel(DialogCreatePass)
        self.lb_info_3.setObjectName(u"lb_info_3")
        self.lb_info_3.setGeometry(QRect(20, 70, 131, 16))
        self.tb_pass1 = QLineEdit(DialogCreatePass)
        self.tb_pass1.setObjectName(u"tb_pass1")
        self.tb_pass1.setGeometry(QRect(170, 40, 281, 22))
        self.tb_pass1.setEchoMode(QLineEdit.EchoMode.Password)
        self.tb_pass2 = QLineEdit(DialogCreatePass)
        self.tb_pass2.setObjectName(u"tb_pass2")
        self.tb_pass2.setGeometry(QRect(170, 70, 281, 22))
        self.tb_pass2.setEchoMode(QLineEdit.EchoMode.Password)
        self.btn_ok = QPushButton(DialogCreatePass)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(350, 110, 101, 24))
        self.btn_cancel = QPushButton(DialogCreatePass)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(242, 110, 101, 24))

        self.retranslateUi(DialogCreatePass)

        QMetaObject.connectSlotsByName(DialogCreatePass)
    # setupUi

    def retranslateUi(self, DialogCreatePass):
        DialogCreatePass.setWindowTitle(QCoreApplication.translate("DialogCreatePass", u"Dialog", None))
        self.lb_info.setText(QCoreApplication.translate("DialogCreatePass", u"label", None))
        self.lb_info_2.setText(QCoreApplication.translate("DialogCreatePass", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.lb_info_3.setText(QCoreApplication.translate("DialogCreatePass", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
        self.btn_ok.setText(QCoreApplication.translate("DialogCreatePass", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.btn_cancel.setText(QCoreApplication.translate("DialogCreatePass", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

