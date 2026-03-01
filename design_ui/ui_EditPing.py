# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditPing.ui'
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

class Ui_DialogEditPing(object):
    def setupUi(self, DialogEditPing):
        if not DialogEditPing.objectName():
            DialogEditPing.setObjectName(u"DialogEditPing")
        DialogEditPing.resize(533, 99)
        self.tb_hostname = QLineEdit(DialogEditPing)
        self.tb_hostname.setObjectName(u"tb_hostname")
        self.tb_hostname.setGeometry(QRect(240, 30, 281, 22))
        self.btn_save_ping = QPushButton(DialogEditPing)
        self.btn_save_ping.setObjectName(u"btn_save_ping")
        self.btn_save_ping.setGeometry(QRect(300, 70, 221, 26))
        self.btn_save = QPushButton(DialogEditPing)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(200, 70, 91, 26))
        self.btn_cancel = QPushButton(DialogEditPing)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(100, 70, 91, 26))
        self.label = QLabel(DialogEditPing)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 171, 20))
        self.lbl_name_net = QLabel(DialogEditPing)
        self.lbl_name_net.setObjectName(u"lbl_name_net")
        self.lbl_name_net.setGeometry(QRect(100, 30, 101, 20))

        self.retranslateUi(DialogEditPing)

        QMetaObject.connectSlotsByName(DialogEditPing)
    # setupUi

    def retranslateUi(self, DialogEditPing):
        DialogEditPing.setWindowTitle(QCoreApplication.translate("DialogEditPing", u"Dialog", None))
        self.btn_save_ping.setText(QCoreApplication.translate("DialogEditPing", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438 \u043f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u0435", None))
        self.btn_save.setText(QCoreApplication.translate("DialogEditPing", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_cancel.setText(QCoreApplication.translate("DialogEditPing", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.label.setText(QCoreApplication.translate("DialogEditPing", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0440\u043e\u0432\u0435\u0440\u043e\u0447\u043d\u044b\u0439 \u0430\u0434\u0440\u0435\u0441", None))
        self.lbl_name_net.setText(QCoreApplication.translate("DialogEditPing", u"\u043b\u043e\u043a\u0430\u043b\u044c\u043d\u043e\u0439 \u0441\u0435\u0442\u0438", None))
    # retranslateUi

