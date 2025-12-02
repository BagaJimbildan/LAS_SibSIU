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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_DialogSuccess(object):
    def setupUi(self, DialogSuccess):
        if not DialogSuccess.objectName():
            DialogSuccess.setObjectName(u"DialogSuccess")
        DialogSuccess.resize(340, 143)
        self.btn_close = QPushButton(DialogSuccess)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(240, 110, 91, 31))
        self.tb_info = QTextEdit(DialogSuccess)
        self.tb_info.setObjectName(u"tb_info")
        self.tb_info.setGeometry(QRect(10, 10, 321, 91))
        self.tb_info.setReadOnly(True)

        self.retranslateUi(DialogSuccess)

        QMetaObject.connectSlotsByName(DialogSuccess)
    # setupUi

    def retranslateUi(self, DialogSuccess):
        DialogSuccess.setWindowTitle(QCoreApplication.translate("DialogSuccess", u"\u0423\u0441\u043f\u0435\u0448\u043d\u043e", None))
        self.btn_close.setText(QCoreApplication.translate("DialogSuccess", u"\u041e\u041a", None))
    # retranslateUi

