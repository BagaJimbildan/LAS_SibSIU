# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DisableUser.ui'
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

class Ui_DialogDisableUser(object):
    def setupUi(self, DialogDisableUser):
        if not DialogDisableUser.objectName():
            DialogDisableUser.setObjectName(u"DialogDisableUser")
        DialogDisableUser.resize(400, 168)
        self.tb_name = QLineEdit(DialogDisableUser)
        self.tb_name.setObjectName(u"tb_name")
        self.tb_name.setGeometry(QRect(10, 40, 271, 31))
        self.label = QLabel(DialogDisableUser)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 361, 16))
        self.btn_ok = QPushButton(DialogDisableUser)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(290, 140, 81, 26))
        self.btn_cancel = QPushButton(DialogDisableUser)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(190, 140, 81, 26))

        self.retranslateUi(DialogDisableUser)

        QMetaObject.connectSlotsByName(DialogDisableUser)
    # setupUi

    def retranslateUi(self, DialogDisableUser):
        DialogDisableUser.setWindowTitle(QCoreApplication.translate("DialogDisableUser", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0441\u043e\u0437\u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.label.setText(QCoreApplication.translate("DialogDisableUser", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.btn_ok.setText(QCoreApplication.translate("DialogDisableUser", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        self.btn_cancel.setText(QCoreApplication.translate("DialogDisableUser", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

