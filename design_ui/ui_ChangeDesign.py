# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChangeDesign.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_DialogChangeDesign(object):
    def setupUi(self, DialogChangeDesign):
        if not DialogChangeDesign.objectName():
            DialogChangeDesign.setObjectName(u"DialogChangeDesign")
        DialogChangeDesign.resize(594, 324)
        self.groupBox = QGroupBox(DialogChangeDesign)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 141, 121))
        self.rb_dark = QRadioButton(self.groupBox)
        self.rb_dark.setObjectName(u"rb_dark")
        self.rb_dark.setGeometry(QRect(10, 80, 121, 36))
        self.rb_white = QRadioButton(self.groupBox)
        self.rb_white.setObjectName(u"rb_white")
        self.rb_white.setGeometry(QRect(10, 40, 121, 36))
        self.groupBox_2 = QGroupBox(DialogChangeDesign)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(190, 20, 391, 241))
        self.rb_teal = QRadioButton(self.groupBox_2)
        self.rb_teal.setObjectName(u"rb_teal")
        self.rb_teal.setGeometry(QRect(20, 40, 151, 36))
        self.rb_amber = QRadioButton(self.groupBox_2)
        self.rb_amber.setObjectName(u"rb_amber")
        self.rb_amber.setGeometry(QRect(20, 80, 151, 36))
        self.rb_blue = QRadioButton(self.groupBox_2)
        self.rb_blue.setObjectName(u"rb_blue")
        self.rb_blue.setGeometry(QRect(20, 120, 151, 36))
        self.rb_cyan = QRadioButton(self.groupBox_2)
        self.rb_cyan.setObjectName(u"rb_cyan")
        self.rb_cyan.setGeometry(QRect(20, 160, 151, 36))
        self.rb_lightgreen = QRadioButton(self.groupBox_2)
        self.rb_lightgreen.setObjectName(u"rb_lightgreen")
        self.rb_lightgreen.setGeometry(QRect(20, 200, 151, 36))
        self.rb_pink = QRadioButton(self.groupBox_2)
        self.rb_pink.setObjectName(u"rb_pink")
        self.rb_pink.setGeometry(QRect(220, 40, 151, 36))
        self.rb_red = QRadioButton(self.groupBox_2)
        self.rb_red.setObjectName(u"rb_red")
        self.rb_red.setGeometry(QRect(220, 120, 151, 36))
        self.rb_yellow = QRadioButton(self.groupBox_2)
        self.rb_yellow.setObjectName(u"rb_yellow")
        self.rb_yellow.setGeometry(QRect(220, 160, 151, 36))
        self.rb_purple = QRadioButton(self.groupBox_2)
        self.rb_purple.setObjectName(u"rb_purple")
        self.rb_purple.setGeometry(QRect(220, 80, 151, 36))
        self.btn_ok = QPushButton(DialogChangeDesign)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(420, 280, 127, 31))
        self.btn_cancel = QPushButton(DialogChangeDesign)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(306, 280, 101, 31))
        QWidget.setTabOrder(self.rb_white, self.rb_dark)
        QWidget.setTabOrder(self.rb_dark, self.rb_teal)
        QWidget.setTabOrder(self.rb_teal, self.rb_amber)
        QWidget.setTabOrder(self.rb_amber, self.rb_blue)
        QWidget.setTabOrder(self.rb_blue, self.rb_cyan)
        QWidget.setTabOrder(self.rb_cyan, self.rb_lightgreen)
        QWidget.setTabOrder(self.rb_lightgreen, self.rb_pink)
        QWidget.setTabOrder(self.rb_pink, self.rb_purple)
        QWidget.setTabOrder(self.rb_purple, self.rb_red)
        QWidget.setTabOrder(self.rb_red, self.rb_yellow)
        QWidget.setTabOrder(self.rb_yellow, self.btn_ok)
        QWidget.setTabOrder(self.btn_ok, self.btn_cancel)

        self.retranslateUi(DialogChangeDesign)

        self.btn_ok.setDefault(True)


        QMetaObject.connectSlotsByName(DialogChangeDesign)
    # setupUi

    def retranslateUi(self, DialogChangeDesign):
        DialogChangeDesign.setWindowTitle(QCoreApplication.translate("DialogChangeDesign", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0442\u0435\u043c\u0443 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None))
        self.groupBox.setTitle(QCoreApplication.translate("DialogChangeDesign", u"\u0422\u0435\u043c\u0430", None))
        self.rb_dark.setText(QCoreApplication.translate("DialogChangeDesign", u"\u0422\u0435\u043c\u043d\u0430\u044f", None))
        self.rb_white.setText(QCoreApplication.translate("DialogChangeDesign", u"\u0421\u0432\u0435\u0442\u043b\u0430\u044f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DialogChangeDesign", u"\u0426\u0432\u0435\u0442", None))
        self.rb_teal.setText(QCoreApplication.translate("DialogChangeDesign", u"\u0421\u0438\u043d\u0435-\u0437\u0435\u043b\u0435\u043d\u044b\u0439", None))
        self.rb_amber.setText(QCoreApplication.translate("DialogChangeDesign", u"\u042f\u043d\u0442\u0430\u0440\u043d\u044b\u0439", None))
        self.rb_blue.setText(QCoreApplication.translate("DialogChangeDesign", u"\u0421\u0438\u043d\u0438\u0439", None))
        self.rb_cyan.setText(QCoreApplication.translate("DialogChangeDesign", u"\u0426\u0438\u0430\u043d", None))
        self.rb_lightgreen.setText(QCoreApplication.translate("DialogChangeDesign", u"\u0421\u0432\u0435\u0442\u043b\u043e-\u0437\u0435\u043b\u0435\u043d\u044b\u0439", None))
        self.rb_pink.setText(QCoreApplication.translate("DialogChangeDesign", u"\u0420\u043e\u0437\u043e\u0432\u044b\u0439", None))
        self.rb_red.setText(QCoreApplication.translate("DialogChangeDesign", u"\u041a\u0440\u0430\u0441\u043d\u044b\u0439", None))
        self.rb_yellow.setText(QCoreApplication.translate("DialogChangeDesign", u"\u0416\u0435\u043b\u0442\u044b\u0439", None))
        self.rb_purple.setText(QCoreApplication.translate("DialogChangeDesign", u"\u0424\u0438\u043e\u043b\u0435\u0442\u043e\u0432\u044b\u0439", None))
        self.btn_ok.setText(QCoreApplication.translate("DialogChangeDesign", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.btn_cancel.setText(QCoreApplication.translate("DialogChangeDesign", u"\u0412\u044b\u0439\u0442\u0438", None))
    # retranslateUi

