# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WriteServer.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_DialogWriteServer(object):
    def setupUi(self, DialogWriteServer):
        if not DialogWriteServer.objectName():
            DialogWriteServer.setObjectName(u"DialogWriteServer")
        DialogWriteServer.resize(299, 118)
        self.label = QLabel(DialogWriteServer)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 281, 16))
        self.btn_yes = QPushButton(DialogWriteServer)
        self.btn_yes.setObjectName(u"btn_yes")
        self.btn_yes.setGeometry(QRect(200, 90, 81, 26))
        self.btn_no = QPushButton(DialogWriteServer)
        self.btn_no.setObjectName(u"btn_no")
        self.btn_no.setGeometry(QRect(110, 90, 81, 26))
        self.cb_asking = QCheckBox(DialogWriteServer)
        self.cb_asking.setObjectName(u"cb_asking")
        self.cb_asking.setGeometry(QRect(40, 60, 251, 24))

        self.retranslateUi(DialogWriteServer)

        QMetaObject.connectSlotsByName(DialogWriteServer)
    # setupUi

    def retranslateUi(self, DialogWriteServer):
        DialogWriteServer.setWindowTitle(QCoreApplication.translate("DialogWriteServer", u"\u0422\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f \u0432\u044b\u0431\u043e\u0440", None))
        self.label.setText(QCoreApplication.translate("DialogWriteServer", u"\u0422\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f \u043b\u0438 \u0437\u0430\u043f\u0438\u0441\u044b\u0432\u0430\u0442\u044c \u0432\u0441\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043d\u0430 \u0441\u0435\u0440\u0432\u0435\u0440?", None))
        self.btn_yes.setText(QCoreApplication.translate("DialogWriteServer", u"\u0414\u0430", None))
        self.btn_no.setText(QCoreApplication.translate("DialogWriteServer", u"\u041d\u0435\u0442", None))
        self.cb_asking.setText(QCoreApplication.translate("DialogWriteServer", u"\u043d\u0435 \u0441\u043f\u0440\u0430\u0448\u0438\u0432\u0430\u0442\u044c \u043f\u0440\u0438 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u043c \u0437\u0430\u043f\u0443\u0441\u043a\u0435", None))
    # retranslateUi

