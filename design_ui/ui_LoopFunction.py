# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoopFunction.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGroupBox,
    QPushButton, QSizePolicy, QWidget)

class Ui_DialogLoopFunction(object):
    def setupUi(self, DialogLoopFunction):
        if not DialogLoopFunction.objectName():
            DialogLoopFunction.setObjectName(u"DialogLoopFunction")
        DialogLoopFunction.resize(399, 395)
        self.groupBox = QGroupBox(DialogLoopFunction)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 351, 281))
        self.cb_admin = QCheckBox(self.groupBox)
        self.cb_admin.setObjectName(u"cb_admin")
        self.cb_admin.setGeometry(QRect(20, 30, 261, 24))
        self.cb_pass_admin = QCheckBox(self.groupBox)
        self.cb_pass_admin.setObjectName(u"cb_pass_admin")
        self.cb_pass_admin.setGeometry(QRect(20, 60, 311, 24))
        self.cb_user = QCheckBox(self.groupBox)
        self.cb_user.setObjectName(u"cb_user")
        self.cb_user.setGeometry(QRect(20, 90, 311, 24))
        self.cb_windows = QCheckBox(self.groupBox)
        self.cb_windows.setObjectName(u"cb_windows")
        self.cb_windows.setGeometry(QRect(20, 120, 311, 24))
        self.cb_office = QCheckBox(self.groupBox)
        self.cb_office.setObjectName(u"cb_office")
        self.cb_office.setGeometry(QRect(20, 150, 311, 24))
        self.cb_name_pc = QCheckBox(self.groupBox)
        self.cb_name_pc.setObjectName(u"cb_name_pc")
        self.cb_name_pc.setGeometry(QRect(20, 180, 311, 24))
        self.cb_domain = QCheckBox(self.groupBox)
        self.cb_domain.setObjectName(u"cb_domain")
        self.cb_domain.setGeometry(QRect(20, 210, 311, 24))
        self.cb_network = QCheckBox(self.groupBox)
        self.cb_network.setObjectName(u"cb_network")
        self.cb_network.setGeometry(QRect(20, 240, 311, 24))
        self.btn_ok = QPushButton(DialogLoopFunction)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(290, 370, 101, 26))
        self.btn_cancel = QPushButton(DialogLoopFunction)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(180, 370, 101, 26))

        self.retranslateUi(DialogLoopFunction)

        QMetaObject.connectSlotsByName(DialogLoopFunction)
    # setupUi

    def retranslateUi(self, DialogLoopFunction):
        DialogLoopFunction.setWindowTitle(QCoreApplication.translate("DialogLoopFunction", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0446\u0438\u043a\u043b\u0430 \u0444\u0443\u043d\u043a\u0446\u0438\u0439", None))
        self.groupBox.setTitle(QCoreApplication.translate("DialogLoopFunction", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0444\u0443\u043d\u043a\u0446\u0438\u0439", None))
        self.cb_admin.setText(QCoreApplication.translate("DialogLoopFunction", u"\u0412\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u0432\u0441\u0442\u0440\u043e\u0435\u043d\u043d\u043e\u0433\u043e \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.cb_pass_admin.setText(QCoreApplication.translate("DialogLoopFunction", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043f\u0430\u0440\u043e\u043b\u044f \u0432\u0441\u0442\u0440\u043e\u0435\u043d\u043d\u043e\u0433\u043e \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.cb_user.setText(QCoreApplication.translate("DialogLoopFunction", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u0441\u043e\u0437\u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.cb_windows.setText(QCoreApplication.translate("DialogLoopFunction", u"\u0410\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u044f Windows", None))
        self.cb_office.setText(QCoreApplication.translate("DialogLoopFunction", u"\u0410\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u044f Office", None))
        self.cb_name_pc.setText(QCoreApplication.translate("DialogLoopFunction", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0438\u043c\u0435\u043d\u0438 \u041f\u041a", None))
        self.cb_domain.setText(QCoreApplication.translate("DialogLoopFunction", u"\u0412\u0432\u043e\u0434 \u0432 \u0434\u043e\u043c\u0435\u043d", None))
        self.cb_network.setText(QCoreApplication.translate("DialogLoopFunction", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u0441\u0435\u0442\u0438", None))
        self.btn_ok.setText(QCoreApplication.translate("DialogLoopFunction", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.btn_cancel.setText(QCoreApplication.translate("DialogLoopFunction", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

