# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window2.ui',
# licensing of 'window2.ui' applies.
#
# Created: Mon Jun  3 20:47:06 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Window2(object):
    def setupUi(self, Window2):
        Window2.setObjectName("Window2")
        Window2.resize(911, 601)
        self.centralwidget = QtWidgets.QWidget(Window2)
        self.centralwidget.setObjectName("centralwidget")
        self.cmdTable = QtWidgets.QTableWidget(self.centralwidget)
        self.cmdTable.setGeometry(QtCore.QRect(10, 10, 831, 461))
        self.cmdTable.setRowCount(10)
        self.cmdTable.setColumnCount(7)
        self.cmdTable.setObjectName("cmdTable")
        self.cmdTable.setColumnCount(7)
        self.cmdTable.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.cmdTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cmdTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cmdTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.cmdTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.cmdTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.cmdTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.cmdTable.setHorizontalHeaderItem(6, item)
        Window2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 21))
        self.menubar.setObjectName("menubar")
        Window2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window2)
        self.statusbar.setObjectName("statusbar")
        Window2.setStatusBar(self.statusbar)

        self.retranslateUi(Window2)
        QtCore.QMetaObject.connectSlotsByName(Window2)

    def retranslateUi(self, Window2):
        Window2.setWindowTitle(QtWidgets.QApplication.translate("Window2", "Command", None, -1))
        self.cmdTable.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Window2", "Command", None, -1))
        self.cmdTable.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Window2", "Command Field", None, -1))
        self.cmdTable.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("Window2", "Default", None, -1))
        self.cmdTable.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("Window2", "Check", None, -1))
        self.cmdTable.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("Window2", "Address", None, -1))
        self.cmdTable.horizontalHeaderItem(5).setText(QtWidgets.QApplication.translate("Window2", "Max", None, -1))
        self.cmdTable.horizontalHeaderItem(6).setText(QtWidgets.QApplication.translate("Window2", "Min", None, -1))

