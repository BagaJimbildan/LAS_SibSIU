# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StandardName.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_DialogStandardName(object):
    def setupUi(self, DialogStandardName):
        if not DialogStandardName.objectName():
            DialogStandardName.setObjectName(u"DialogStandardName")
        DialogStandardName.resize(837, 188)
        self.label = QLabel(DialogStandardName)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 261, 16))
        self.label_2 = QLabel(DialogStandardName)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 90, 261, 16))
        self.tb_num_cab = QLineEdit(DialogStandardName)
        self.tb_num_cab.setObjectName(u"tb_num_cab")
        self.tb_num_cab.setGeometry(QRect(290, 60, 191, 22))
        self.tb_num_inv = QLineEdit(DialogStandardName)
        self.tb_num_inv.setObjectName(u"tb_num_inv")
        self.tb_num_inv.setGeometry(QRect(290, 90, 191, 22))
        self.cb_type = QComboBox(DialogStandardName)
        self.cb_type.setObjectName(u"cb_type")
        self.cb_type.setGeometry(QRect(290, 120, 191, 24))
        self.label_3 = QLabel(DialogStandardName)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 120, 261, 16))
        self.btn_ok = QPushButton(DialogStandardName)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(390, 160, 101, 24))
        self.btn_cancel = QPushButton(DialogStandardName)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(280, 160, 101, 24))
        self.lb_info = QLabel(DialogStandardName)
        self.lb_info.setObjectName(u"lb_info")
        self.lb_info.setGeometry(QRect(10, 10, 481, 20))
        self.lbl_error_num_cab = QLabel(DialogStandardName)
        self.lbl_error_num_cab.setObjectName(u"lbl_error_num_cab")
        self.lbl_error_num_cab.setGeometry(QRect(490, 60, 341, 16))
        self.lbl_error_num_inv = QLabel(DialogStandardName)
        self.lbl_error_num_inv.setObjectName(u"lbl_error_num_inv")
        self.lbl_error_num_inv.setGeometry(QRect(490, 90, 341, 16))

        self.retranslateUi(DialogStandardName)

        QMetaObject.connectSlotsByName(DialogStandardName)
    # setupUi

    def retranslateUi(self, DialogStandardName):
        DialogStandardName.setWindowTitle(QCoreApplication.translate("DialogStandardName", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0438\u043c\u0435\u043d\u0438 \u041f\u041a", None))
        self.label.setText(QCoreApplication.translate("DialogStandardName", u"\u041d\u043e\u043c\u0435\u0440 \u043a\u0430\u0431\u0438\u043d\u0435\u0442\u0430 (\u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u043c\u0435\u0449\u0435\u043d\u0438\u044f)", None))
        self.label_2.setText(QCoreApplication.translate("DialogStandardName", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 5 \u0446\u0438\u0444\u0440 \u0438\u043d\u0432. \u043d\u043e\u043c\u0435\u0440\u0430 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u0430", None))
        self.label_3.setText(QCoreApplication.translate("DialogStandardName", u"\u0422\u0438\u043f \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430", None))
        self.btn_ok.setText(QCoreApplication.translate("DialogStandardName", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.btn_cancel.setText(QCoreApplication.translate("DialogStandardName", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.lb_info.setText(QCoreApplication.translate("DialogStandardName", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f \u0438\u043c\u0435\u043d\u0438 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u0430 \u043f\u043e \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u0443", None))
        self.lbl_error_num_cab.setText(QCoreApplication.translate("DialogStandardName", u"\u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0437\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.lbl_error_num_inv.setText(QCoreApplication.translate("DialogStandardName", u"\u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0437\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
    # retranslateUi

