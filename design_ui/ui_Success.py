# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Success.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_DialogSuccess(object):
    def setupUi(self, DialogSuccess):
        if not DialogSuccess.objectName():
            DialogSuccess.setObjectName(u"DialogSuccess")
        DialogSuccess.resize(340, 73)
        self.btn_close = QPushButton(DialogSuccess)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(250, 40, 91, 31))
        self.lb_info = QLabel(DialogSuccess)
        self.lb_info.setObjectName(u"lb_info")
        self.lb_info.setGeometry(QRect(10, 10, 321, 16))

        self.retranslateUi(DialogSuccess)

        QMetaObject.connectSlotsByName(DialogSuccess)
    # setupUi

    def retranslateUi(self, DialogSuccess):
        DialogSuccess.setWindowTitle(QCoreApplication.translate("DialogSuccess", u"\u0423\u0441\u043f\u0435\u0448\u043d\u043e", None))
        self.btn_close.setText(QCoreApplication.translate("DialogSuccess", u"\u041e\u041a", None))
        self.lb_info.setText(QCoreApplication.translate("DialogSuccess", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c:", None))
    # retranslateUi

