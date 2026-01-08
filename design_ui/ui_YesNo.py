# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'YesNo.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_DialogYesNo(object):
    def setupUi(self, DialogYesNo):
        if not DialogYesNo.objectName():
            DialogYesNo.setObjectName(u"DialogYesNo")
        DialogYesNo.resize(324, 236)
        self.tb_text = QTextEdit(DialogYesNo)
        self.tb_text.setObjectName(u"tb_text")
        self.tb_text.setGeometry(QRect(10, 30, 301, 161))
        self.tb_text.setReadOnly(True)
        self.btn_ok = QPushButton(DialogYesNo)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(220, 200, 91, 31))
        self.btn_close = QPushButton(DialogYesNo)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(120, 200, 91, 31))

        self.retranslateUi(DialogYesNo)

        QMetaObject.connectSlotsByName(DialogYesNo)
    # setupUi

    def retranslateUi(self, DialogYesNo):
        DialogYesNo.setWindowTitle(QCoreApplication.translate("DialogYesNo", u"\u0412\u044b \u0443\u0432\u0435\u0440\u0435\u043d\u044b?", None))
        self.btn_ok.setText(QCoreApplication.translate("DialogYesNo", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.btn_close.setText(QCoreApplication.translate("DialogYesNo", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

