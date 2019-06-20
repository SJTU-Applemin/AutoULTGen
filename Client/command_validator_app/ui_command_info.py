# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'command_info.ui',
# licensing of 'command_info.ui' applies.
#
# Created: Mon Jun 10 00:20:41 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_FormCommandInfo(object):
    def setupUi(self, FormCommandInfo):
        FormCommandInfo.setObjectName("FormCommandInfo")
        FormCommandInfo.resize(1367, 741)
        self.treeWidgetCmd = QtWidgets.QTreeWidget(FormCommandInfo)
        self.treeWidgetCmd.setGeometry(QtCore.QRect(0, 0, 261, 741))
        self.treeWidgetCmd.setWordWrap(False)
        self.treeWidgetCmd.setColumnCount(1)
        self.treeWidgetCmd.setObjectName("treeWidgetCmd")
        self.treeWidgetCmd.headerItem().setText(0, "1")
        self.treeWidgetCmd.header().setVisible(False)
        self.tableWidgetCmd = QtWidgets.QTableWidget(FormCommandInfo)
        self.tableWidgetCmd.setGeometry(QtCore.QRect(260, 0, 1111, 691))
        self.tableWidgetCmd.setObjectName("tableWidgetCmd")
        self.tableWidgetCmd.setColumnCount(11)
        self.tableWidgetCmd.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCmd.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCmd.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCmd.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCmd.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCmd.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCmd.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCmd.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCmd.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCmd.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCmd.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCmd.setHorizontalHeaderItem(10, item)
        self.pushButtonSave = QtWidgets.QPushButton(FormCommandInfo)
        self.pushButtonSave.setGeometry(QtCore.QRect(880, 700, 121, 41))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonGen = QtWidgets.QPushButton(FormCommandInfo)
        self.pushButtonGen.setGeometry(QtCore.QRect(1020, 700, 121, 41))
        self.pushButtonGen.setObjectName("pushButtonGen")
        self.checkBoxReserved = QtWidgets.QCheckBox(FormCommandInfo)
        self.checkBoxReserved.setGeometry(QtCore.QRect(290, 710, 161, 17))
        self.checkBoxReserved.setChecked(True)
        self.checkBoxReserved.setObjectName("checkBoxReserved")
        self.checkBoxHex = QtWidgets.QCheckBox(FormCommandInfo)
        self.checkBoxHex.setGeometry(QtCore.QRect(420, 710, 81, 17))
        self.checkBoxHex.setChecked(True)
        self.checkBoxHex.setObjectName("checkBoxHex")
        self.checkBoxDec = QtWidgets.QCheckBox(FormCommandInfo)
        self.checkBoxDec.setGeometry(QtCore.QRect(515, 710, 71, 17))
        self.checkBoxDec.setObjectName("checkBoxDec")
        self.checkBoxBinary = QtWidgets.QCheckBox(FormCommandInfo)
        self.checkBoxBinary.setGeometry(QtCore.QRect(590, 710, 70, 17))
        self.checkBoxBinary.setObjectName("checkBoxBinary")

        self.retranslateUi(FormCommandInfo)
        QtCore.QMetaObject.connectSlotsByName(FormCommandInfo)

    def retranslateUi(self, FormCommandInfo):
        FormCommandInfo.setWindowTitle(QtWidgets.QApplication.translate("FormCommandInfo", "Form", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Command", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Dword", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Field", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Default", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Value", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(5).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Check", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(6).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Address", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(7).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Min", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(8).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Max", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(9).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Bitfield_low", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(10).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Bitfield_high", None, -1))
        self.pushButtonSave.setText(QtWidgets.QApplication.translate("FormCommandInfo", "Save", None, -1))
        self.pushButtonGen.setText(QtWidgets.QApplication.translate("FormCommandInfo", "Generate", None, -1))
        self.checkBoxReserved.setText(QtWidgets.QApplication.translate("FormCommandInfo", "Hide reserved field", None, -1))
        self.checkBoxHex.setText(QtWidgets.QApplication.translate("FormCommandInfo", "Hexadecimal", None, -1))
        self.checkBoxDec.setText(QtWidgets.QApplication.translate("FormCommandInfo", "Decimal", None, -1))
        self.checkBoxBinary.setText(QtWidgets.QApplication.translate("FormCommandInfo", "Binary", None, -1))

