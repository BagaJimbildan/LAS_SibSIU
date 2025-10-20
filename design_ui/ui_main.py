# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1051, 596)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 110, 51, 16))
        self.lbl_domen = QLabel(self.centralwidget)
        self.lbl_domen.setObjectName(u"lbl_domen")
        self.lbl_domen.setGeometry(QRect(80, 110, 141, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 30, 51, 16))
        self.lbl_os = QLabel(self.centralwidget)
        self.lbl_os.setObjectName(u"lbl_os")
        self.lbl_os.setGeometry(QRect(80, 30, 221, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 50, 71, 16))
        self.lbl_os_activate = QLabel(self.centralwidget)
        self.lbl_os_activate.setObjectName(u"lbl_os_activate")
        self.lbl_os_activate.setGeometry(QRect(90, 50, 181, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 140, 51, 16))
        self.lbl_dhcp = QLabel(self.centralwidget)
        self.lbl_dhcp.setObjectName(u"lbl_dhcp")
        self.lbl_dhcp.setGeometry(QRect(80, 140, 161, 16))
        self.btn_net_1 = QPushButton(self.centralwidget)
        self.btn_net_1.setObjectName(u"btn_net_1")
        self.btn_net_1.setGeometry(QRect(10, 160, 111, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1051, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u0435\u043d: ", None))
        self.lbl_domen.setText(QCoreApplication.translate("MainWindow", u"???", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0421:", None))
        self.lbl_os.setText(QCoreApplication.translate("MainWindow", u"??????????????????????????????????????", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0438\u0432\u0430\u0446\u0438\u044f:", None))
        self.lbl_os_activate.setText(QCoreApplication.translate("MainWindow", u"???", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DHCP", None))
        self.lbl_dhcp.setText(QCoreApplication.translate("MainWindow", u"???", None))
        self.btn_net_1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0441\u0435\u0442\u0438", None))
    # retranslateUi

