# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 0, 351, 81))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.txtLocation = QTextEdit(Widget)
        self.txtLocation.setObjectName(u"txtLocation")
        self.txtLocation.setGeometry(QRect(140, 90, 601, 31))
        self.btnScan = QPushButton(Widget)
        self.btnScan.setObjectName(u"btnScan")
        self.btnScan.setGeometry(QRect(350, 548, 91, 41))
        self.lstLog = QListWidget(Widget)
        self.lstLog.setObjectName(u"lstLog")
        self.lstLog.setGeometry(QRect(50, 210, 701, 331))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 170, 63, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 90, 91, 31))
        self.label_3.setFont(font1)
        self.btnBrowse = QPushButton(Widget)
        self.btnBrowse.setObjectName(u"btnBrowse")
        self.btnBrowse.setGeometry(QRect(652, 130, 91, 41))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Image Dataset Validator", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Image Dataset Validator", None))
        self.btnScan.setText(QCoreApplication.translate("Widget", u"Scan", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Log:", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Location: ", None))
        self.btnBrowse.setText(QCoreApplication.translate("Widget", u"Browse", None))
    # retranslateUi

