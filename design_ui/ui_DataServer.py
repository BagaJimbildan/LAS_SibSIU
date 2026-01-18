# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataServer.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_DialogDataServer(object):
    def setupUi(self, DialogDataServer):
        if not DialogDataServer.objectName():
            DialogDataServer.setObjectName(u"DialogDataServer")
        DialogDataServer.resize(469, 346)
        self.groupBox = QGroupBox(DialogDataServer)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 401, 101))
        self.tb_username = QLineEdit(self.groupBox)
        self.tb_username.setObjectName(u"tb_username")
        self.tb_username.setGeometry(QRect(160, 60, 221, 22))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 141, 16))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 101, 16))
        self.tb_server = QLineEdit(self.groupBox)
        self.tb_server.setObjectName(u"tb_server")
        self.tb_server.setGeometry(QRect(160, 30, 221, 22))
        self.label_3 = QLabel(DialogDataServer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 170, 141, 16))
        self.tb_owner = QLineEdit(DialogDataServer)
        self.tb_owner.setObjectName(u"tb_owner")
        self.tb_owner.setGeometry(QRect(170, 170, 221, 22))
        self.label_4 = QLabel(DialogDataServer)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 140, 101, 16))
        self.tb_ticket = QLineEdit(DialogDataServer)
        self.tb_ticket.setObjectName(u"tb_ticket")
        self.tb_ticket.setGeometry(QRect(170, 140, 221, 22))
        self.label_5 = QLabel(DialogDataServer)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 200, 141, 16))
        self.tb_subdivision = QLineEdit(DialogDataServer)
        self.tb_subdivision.setObjectName(u"tb_subdivision")
        self.tb_subdivision.setGeometry(QRect(170, 200, 221, 22))
        self.label_6 = QLabel(DialogDataServer)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 230, 141, 16))
        self.label_7 = QLabel(DialogDataServer)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 260, 141, 16))
        self.tb_current_room = QLineEdit(DialogDataServer)
        self.tb_current_room.setObjectName(u"tb_current_room")
        self.tb_current_room.setGeometry(QRect(170, 260, 221, 22))
        self.tb_room = QLineEdit(DialogDataServer)
        self.tb_room.setObjectName(u"tb_room")
        self.tb_room.setGeometry(QRect(170, 230, 221, 22))
        self.btn_ok = QPushButton(DialogDataServer)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(380, 320, 81, 26))
        self.btn_cancel = QPushButton(DialogDataServer)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(160, 320, 211, 26))

        self.retranslateUi(DialogDataServer)

        QMetaObject.connectSlotsByName(DialogDataServer)
    # setupUi

    def retranslateUi(self, DialogDataServer):
        DialogDataServer.setWindowTitle(QCoreApplication.translate("DialogDataServer", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.groupBox.setTitle(QCoreApplication.translate("DialogDataServer", u"\u0421\u0435\u0440\u0432\u0435\u0440", None))
        self.label_2.setText(QCoreApplication.translate("DialogDataServer", u"\u041b\u043e\u0433\u0438\u043d \u0434\u043b\u044f \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("DialogDataServer", u"\u0424\u0430\u0439\u043b \u043d\u0430 \u0441\u0435\u0440\u0432\u0435\u0440\u0435", None))
        self.label_3.setText(QCoreApplication.translate("DialogDataServer", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c \u041f\u041a", None))
        self.label_4.setText(QCoreApplication.translate("DialogDataServer", u"\u0417\u0430\u044f\u0432\u043a\u0430", None))
        self.label_5.setText(QCoreApplication.translate("DialogDataServer", u"\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.label_6.setText(QCoreApplication.translate("DialogDataServer", u"\u041a\u0430\u0431\u0438\u043d\u0435\u0442", None))
        self.label_7.setText(QCoreApplication.translate("DialogDataServer", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u043a\u0430\u0431\u0438\u043d\u0435\u0442", None))
        self.btn_ok.setText(QCoreApplication.translate("DialogDataServer", u"OK", None))
        self.btn_cancel.setText(QCoreApplication.translate("DialogDataServer", u"\u041d\u0435 \u0437\u0430\u043f\u0438\u0441\u044b\u0432\u0430\u0442\u044c \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043d\u0430 \u0441\u0435\u0440\u0432\u0435\u0440", None))
    # retranslateUi

