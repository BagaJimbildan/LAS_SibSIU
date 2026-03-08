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
        DialogYesNo.resize(324, 115)
        self.tb_text = QTextEdit(DialogYesNo)
        self.tb_text.setObjectName(u"tb_text")
        self.tb_text.setGeometry(QRect(10, 10, 301, 61))
        self.tb_text.setReadOnly(True)
        self.btn_ok = QPushButton(DialogYesNo)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(180, 80, 131, 31))
        self.btn_close = QPushButton(DialogYesNo)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(80, 80, 91, 31))

        self.retranslateUi(DialogYesNo)

        self.btn_ok.setDefault(True)


        QMetaObject.connectSlotsByName(DialogYesNo)
    # setupUi

    def retranslateUi(self, DialogYesNo):
        DialogYesNo.setWindowTitle(QCoreApplication.translate("DialogYesNo", u"\u0412\u044b \u0443\u0432\u0435\u0440\u0435\u043d\u044b?", None))
        self.tb_text.setHtml(QCoreApplication.translate("DialogYesNo", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:13px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.btn_ok.setText(QCoreApplication.translate("DialogYesNo", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.btn_close.setText(QCoreApplication.translate("DialogYesNo", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

