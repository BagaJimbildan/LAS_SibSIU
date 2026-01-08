# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DomainName.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_DialogDomainName(object):
    def setupUi(self, DialogDomainName):
        if not DialogDomainName.objectName():
            DialogDomainName.setObjectName(u"DialogDomainName")
        DialogDomainName.resize(352, 106)
        self.btn_ok = QPushButton(DialogDomainName)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(240, 70, 101, 26))
        self.btn_cancel = QPushButton(DialogDomainName)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(150, 70, 81, 26))
        self.tb_name = QLineEdit(DialogDomainName)
        self.tb_name.setObjectName(u"tb_name")
        self.tb_name.setGeometry(QRect(20, 20, 321, 31))

        self.retranslateUi(DialogDomainName)

        QMetaObject.connectSlotsByName(DialogDomainName)
    # setupUi

    def retranslateUi(self, DialogDomainName):
        DialogDomainName.setWindowTitle(QCoreApplication.translate("DialogDomainName", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u0434\u043e\u043c\u0435\u043d\u0430", None))
        self.btn_ok.setText(QCoreApplication.translate("DialogDomainName", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u0441\u044f", None))
        self.btn_cancel.setText(QCoreApplication.translate("DialogDomainName", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

