# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ParamNet.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_DialogParamNet(object):
    def setupUi(self, DialogParamNet):
        if not DialogParamNet.objectName():
            DialogParamNet.setObjectName(u"DialogParamNet")
        DialogParamNet.resize(277, 161)
        self.label = QLabel(DialogParamNet)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 61, 20))
        self.lbl_ip = QLabel(DialogParamNet)
        self.lbl_ip.setObjectName(u"lbl_ip")
        self.lbl_ip.setGeometry(QRect(130, 10, 141, 16))
        self.lbl_mask = QLabel(DialogParamNet)
        self.lbl_mask.setObjectName(u"lbl_mask")
        self.lbl_mask.setGeometry(QRect(130, 30, 141, 16))
        self.label_2 = QLabel(DialogParamNet)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 30, 101, 20))
        self.label_3 = QLabel(DialogParamNet)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 50, 101, 20))
        self.lbl_gateway = QLabel(DialogParamNet)
        self.lbl_gateway.setObjectName(u"lbl_gateway")
        self.lbl_gateway.setGeometry(QRect(130, 50, 141, 16))
        self.label_4 = QLabel(DialogParamNet)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 70, 101, 20))
        self.lbl_dns1 = QLabel(DialogParamNet)
        self.lbl_dns1.setObjectName(u"lbl_dns1")
        self.lbl_dns1.setGeometry(QRect(130, 70, 141, 16))
        self.lbl_dns2 = QLabel(DialogParamNet)
        self.lbl_dns2.setObjectName(u"lbl_dns2")
        self.lbl_dns2.setGeometry(QRect(130, 90, 141, 16))
        self.label_5 = QLabel(DialogParamNet)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 90, 101, 20))
        self.btn_ok = QPushButton(DialogParamNet)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(185, 120, 81, 31))

        self.retranslateUi(DialogParamNet)

        QMetaObject.connectSlotsByName(DialogParamNet)
    # setupUi

    def retranslateUi(self, DialogParamNet):
        DialogParamNet.setWindowTitle(QCoreApplication.translate("DialogParamNet", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0441\u0435\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("DialogParamNet", u"IP \u0430\u0434\u0440\u0435\u0441:", None))
        self.lbl_ip.setText(QCoreApplication.translate("DialogParamNet", u"???", None))
        self.lbl_mask.setText(QCoreApplication.translate("DialogParamNet", u"???", None))
        self.label_2.setText(QCoreApplication.translate("DialogParamNet", u"\u041c\u0430\u0441\u043a\u0430 \u043f\u043e\u0434\u0441\u0435\u0442\u0438:", None))
        self.label_3.setText(QCoreApplication.translate("DialogParamNet", u"\u0428\u043b\u044e\u0437:", None))
        self.lbl_gateway.setText(QCoreApplication.translate("DialogParamNet", u"???", None))
        self.label_4.setText(QCoreApplication.translate("DialogParamNet", u"DNS_1:", None))
        self.lbl_dns1.setText(QCoreApplication.translate("DialogParamNet", u"???", None))
        self.lbl_dns2.setText(QCoreApplication.translate("DialogParamNet", u"???", None))
        self.label_5.setText(QCoreApplication.translate("DialogParamNet", u"DNS_2:", None))
        self.btn_ok.setText(QCoreApplication.translate("DialogParamNet", u"\u041e\u041a", None))
    # retranslateUi

