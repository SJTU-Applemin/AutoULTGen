﻿# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\command_info.ui',
# licensing of '.\command_info.ui' applies.
#
# Created: Thu Aug  8 14:33:10 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_FormCommandInfo(object):
    def setupUi(self, FormCommandInfo):
        FormCommandInfo.setObjectName("FormCommandInfo")
        FormCommandInfo.resize(1463, 759)
        FormCommandInfo.setAcceptDrops(False)
        self.gridLayout_2 = QtWidgets.QGridLayout(FormCommandInfo)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(FormCommandInfo)
        self.stackedWidget.setObjectName("stackedWidget")
        self.All = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.All.sizePolicy().hasHeightForWidth())
        self.All.setSizePolicy(sizePolicy)
        self.All.setObjectName("All")
        self.gridLayout = QtWidgets.QGridLayout(self.All)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.treeWidgetCmd = QtWidgets.QTreeWidget(self.All)
        self.treeWidgetCmd.setHeaderHidden(True)
        self.treeWidgetCmd.setObjectName("treeWidgetCmd")
        self.treeWidgetCmd.headerItem().setText(0, "1")
        self.horizontalLayout_3.addWidget(self.treeWidgetCmd)
        self.tableWidgetCmd = QtWidgets.QTableWidget(self.All)
        self.tableWidgetCmd.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
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
        self.tableWidgetCmd.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetCmd.verticalHeader().setCascadingSectionResizes(True)
        self.horizontalLayout_3.addWidget(self.tableWidgetCmd)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBoxReserved = QtWidgets.QCheckBox(self.All)
        self.checkBoxReserved.setChecked(True)
        self.checkBoxReserved.setObjectName("checkBoxReserved")
        self.horizontalLayout.addWidget(self.checkBoxReserved)
        self.checkBoxHex = QtWidgets.QCheckBox(self.All)
        self.checkBoxHex.setChecked(True)
        self.checkBoxHex.setObjectName("checkBoxHex")
        self.horizontalLayout.addWidget(self.checkBoxHex)
        self.checkBoxDec = QtWidgets.QCheckBox(self.All)
        self.checkBoxDec.setObjectName("checkBoxDec")
        self.horizontalLayout.addWidget(self.checkBoxDec)
        self.checkBoxBinary = QtWidgets.QCheckBox(self.All)
        self.checkBoxBinary.setObjectName("checkBoxBinary")
        self.horizontalLayout.addWidget(self.checkBoxBinary)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.pushButtonSCL = QtWidgets.QPushButton(self.All)
        self.pushButtonSCL.setObjectName("pushButtonSCL")
        self.horizontalLayout_2.addWidget(self.pushButtonSCL)
        self.pushButtonGen = QtWidgets.QPushButton(self.All)
        self.pushButtonGen.setObjectName("pushButtonGen")
        self.horizontalLayout_2.addWidget(self.pushButtonGen)
        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.All)
        self.cmdlist = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmdlist.sizePolicy().hasHeightForWidth())
        self.cmdlist.setSizePolicy(sizePolicy)
        self.cmdlist.setMinimumSize(QtCore.QSize(1451, 0))
        self.cmdlist.setObjectName("cmdlist")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.cmdlist)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.treeView = QtWidgets.QTreeView(self.cmdlist)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout_5.addWidget(self.treeView)
        self.tableWidgetCmdlist = QtWidgets.QTableWidget(self.cmdlist)
        self.tableWidgetCmdlist.setMaximumSize(QtCore.QSize(2751, 3691))
        self.tableWidgetCmdlist.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidgetCmdlist.setObjectName("tableWidgetCmdlist")
        self.tableWidgetCmdlist.setColumnCount(4)
        self.tableWidgetCmdlist.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCmdlist.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCmdlist.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCmdlist.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCmdlist.setHorizontalHeaderItem(3, item)
        self.tableWidgetCmdlist.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetCmdlist.verticalHeader().setCascadingSectionResizes(True)
        self.horizontalLayout_5.addWidget(self.tableWidgetCmdlist)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButtonSU = QtWidgets.QPushButton(self.cmdlist)
        self.pushButtonSU.setObjectName("pushButtonSU")
        self.horizontalLayout_4.addWidget(self.pushButtonSU, alignment=QtCore.Qt.AlignHCenter)
        self.pushButtonSA = QtWidgets.QPushButton(self.cmdlist)
        self.pushButtonSA.setObjectName("pushButtonSA")
        self.horizontalLayout_4.addWidget(self.pushButtonSA, alignment=QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.cmdlist)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setAcceptDrops(True)
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.retranslateUi(FormCommandInfo)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FormCommandInfo)

    def retranslateUi(self, FormCommandInfo):
        FormCommandInfo.setWindowTitle(QtWidgets.QApplication.translate("FormCommandInfo", "Form", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Command", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Dword", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Field", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Bitfield_low", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Bitfield_high", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(5).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Default", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(6).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Value", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(7).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Check", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(8).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Address", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(9).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Min", None, -1))
        self.tableWidgetCmd.horizontalHeaderItem(10).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Max", None, -1))
        self.checkBoxReserved.setText(QtWidgets.QApplication.translate("FormCommandInfo", "Hide reserved field", None, -1))
        self.checkBoxHex.setText(QtWidgets.QApplication.translate("FormCommandInfo", "Hexadecimal", None, -1))
        self.checkBoxDec.setText(QtWidgets.QApplication.translate("FormCommandInfo", "Decimal", None, -1))
        self.checkBoxBinary.setText(QtWidgets.QApplication.translate("FormCommandInfo", "Binary", None, -1))
        self.pushButtonSCL.setText(QtWidgets.QApplication.translate("FormCommandInfo", "Show CMD List", None, -1))
        self.pushButtonGen.setText(QtWidgets.QApplication.translate("FormCommandInfo", "Generate", None, -1))
        self.tableWidgetCmdlist.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Command", None, -1))
        self.tableWidgetCmdlist.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Class", None, -1))
        self.tableWidgetCmdlist.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("FormCommandInfo", "HitCount", None, -1))
        self.tableWidgetCmdlist.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("FormCommandInfo", "Error", None, -1))
        self.pushButtonSU.setText(QtWidgets.QApplication.translate("FormCommandInfo", "Save Changes && Update", None, -1))
        self.pushButtonSA.setText(QtWidgets.QApplication.translate("FormCommandInfo", "Show All", None, -1))

