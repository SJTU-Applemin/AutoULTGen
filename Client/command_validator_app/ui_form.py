# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui',
# licensing of 'form.ui' applies.
#
# Created: Thu May 23 14:33:42 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1064, 712)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1041, 681))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonSave = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSave.sizePolicy().hasHeightForWidth())
        self.pushButtonSave.setSizePolicy(sizePolicy)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.gridLayout.addWidget(self.pushButtonSave, 0, 0, 1, 1)
        self.cmdTable = QtWidgets.QTableWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmdTable.sizePolicy().hasHeightForWidth())
        self.cmdTable.setSizePolicy(sizePolicy)
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
        self.gridLayout.addWidget(self.cmdTable, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.pushButtonSave.setText(QtWidgets.QApplication.translate("Form", "Save", None, -1))
        self.cmdTable.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Form", "Command", None, -1))
        self.cmdTable.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Form", "Command Field", None, -1))
        self.cmdTable.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("Form", "Default", None, -1))
        self.cmdTable.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("Form", "Check", None, -1))
        self.cmdTable.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("Form", "Address", None, -1))
        self.cmdTable.horizontalHeaderItem(5).setText(QtWidgets.QApplication.translate("Form", "Max", None, -1))
        self.cmdTable.horizontalHeaderItem(6).setText(QtWidgets.QApplication.translate("Form", "Min", None, -1))

