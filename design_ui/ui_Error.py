# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Error.ui'
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

class Ui_DialogError(object):
    def setupUi(self, DialogError):
        if not DialogError.objectName():
            DialogError.setObjectName(u"DialogError")
        DialogError.resize(329, 211)
        self.tb_error = QTextEdit(DialogError)
        self.tb_error.setObjectName(u"tb_error")
        self.tb_error.setGeometry(QRect(10, 20, 311, 151))
        self.tb_error.setReadOnly(True)
        self.btn_close = QPushButton(DialogError)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(230, 180, 91, 31))

        self.retranslateUi(DialogError)

        QMetaObject.connectSlotsByName(DialogError)
    # setupUi

    def retranslateUi(self, DialogError):
        DialogError.setWindowTitle(QCoreApplication.translate("DialogError", u"\u041e\u0448\u0438\u0431\u043a\u0430", None))
        self.btn_close.setText(QCoreApplication.translate("DialogError", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

