# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditNetwork.ui'
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

class Ui_DialogEditNetwork(object):
    def setupUi(self, DialogEditNetwork):
        if not DialogEditNetwork.objectName():
            DialogEditNetwork.setObjectName(u"DialogEditNetwork")
        DialogEditNetwork.resize(355, 141)
        self.lbl_name_is_standart = QLabel(DialogEditNetwork)
        self.lbl_name_is_standart.setObjectName(u"lbl_name_is_standart")
        self.lbl_name_is_standart.setGeometry(QRect(110, 10, 141, 16))
        self.tb_ip1 = QLineEdit(DialogEditNetwork)
        self.tb_ip1.setObjectName(u"tb_ip1")
        self.tb_ip1.setGeometry(QRect(10, 50, 61, 22))
        self.tb_ip1.setMaxLength(3)
        self.lbl_name_is_standart_2 = QLabel(DialogEditNetwork)
        self.lbl_name_is_standart_2.setObjectName(u"lbl_name_is_standart_2")
        self.lbl_name_is_standart_2.setGeometry(QRect(80, 30, 21, 41))
        font = QFont()
        font.setPointSize(26)
        self.lbl_name_is_standart_2.setFont(font)
        self.lbl_name_is_standart_3 = QLabel(DialogEditNetwork)
        self.lbl_name_is_standart_3.setObjectName(u"lbl_name_is_standart_3")
        self.lbl_name_is_standart_3.setGeometry(QRect(170, 30, 21, 41))
        self.lbl_name_is_standart_3.setFont(font)
        self.tb_ip2 = QLineEdit(DialogEditNetwork)
        self.tb_ip2.setObjectName(u"tb_ip2")
        self.tb_ip2.setGeometry(QRect(100, 50, 61, 22))
        self.tb_ip2.setMaxLength(3)
        self.lbl_name_is_standart_4 = QLabel(DialogEditNetwork)
        self.lbl_name_is_standart_4.setObjectName(u"lbl_name_is_standart_4")
        self.lbl_name_is_standart_4.setGeometry(QRect(260, 30, 21, 41))
        self.lbl_name_is_standart_4.setFont(font)
        self.tb_ip3 = QLineEdit(DialogEditNetwork)
        self.tb_ip3.setObjectName(u"tb_ip3")
        self.tb_ip3.setGeometry(QRect(190, 50, 61, 22))
        self.tb_ip3.setMaxLength(3)
        self.tb_ip4 = QLineEdit(DialogEditNetwork)
        self.tb_ip4.setObjectName(u"tb_ip4")
        self.tb_ip4.setGeometry(QRect(280, 50, 61, 22))
        self.tb_ip4.setMaxLength(3)
        self.btn_ok = QPushButton(DialogEditNetwork)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(260, 110, 91, 24))
        self.btn_cancel = QPushButton(DialogEditNetwork)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(160, 110, 91, 24))
        self.lbl_name_is_standart_5 = QLabel(DialogEditNetwork)
        self.lbl_name_is_standart_5.setObjectName(u"lbl_name_is_standart_5")
        self.lbl_name_is_standart_5.setGeometry(QRect(40, 80, 301, 20))

        self.retranslateUi(DialogEditNetwork)

        QMetaObject.connectSlotsByName(DialogEditNetwork)
    # setupUi

    def retranslateUi(self, DialogEditNetwork):
        DialogEditNetwork.setWindowTitle(QCoreApplication.translate("DialogEditNetwork", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u0441\u0435\u0442\u0438", None))
        self.lbl_name_is_standart.setText(QCoreApplication.translate("DialogEditNetwork", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u0432\u044b\u0439 ip \u0430\u0434\u0440\u0435\u0441", None))
        self.lbl_name_is_standart_2.setText(QCoreApplication.translate("DialogEditNetwork", u".", None))
        self.lbl_name_is_standart_3.setText(QCoreApplication.translate("DialogEditNetwork", u".", None))
        self.lbl_name_is_standart_4.setText(QCoreApplication.translate("DialogEditNetwork", u".", None))
        self.btn_ok.setText(QCoreApplication.translate("DialogEditNetwork", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.btn_cancel.setText(QCoreApplication.translate("DialogEditNetwork", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.lbl_name_is_standart_5.setText(QCoreApplication.translate("DialogEditNetwork", u"\u041e\u0441\u0442\u0430\u043b\u044c\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043d\u0430\u0441\u0442\u0440\u043e\u044f\u0442\u0441\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438", None))
    # retranslateUi

