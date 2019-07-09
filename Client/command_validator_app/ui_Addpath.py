# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Addpath.ui',
# licensing of 'Addpath.ui' applies.
#
# Created: Tue Jul  9 16:29:39 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Addpath(object):
    def setupUi(self, Addpath):
        Addpath.setObjectName("Addpath")
        Addpath.resize(807, 516)
        Addpath.setAcceptDrops(False)
        self.listWidget = QtWidgets.QListWidget(Addpath)
        self.listWidget.setGeometry(QtCore.QRect(190, 70, 561, 381))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(Addpath)
        self.label.setGeometry(QtCore.QRect(210, 50, 531, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Addpath)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 80, 111, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButtonAF = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonAF.setObjectName("pushButtonAF")
        self.verticalLayout_2.addWidget(self.pushButtonAF)
        self.pushButtonRemove = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonRemove.setObjectName("pushButtonRemove")
        self.verticalLayout_2.addWidget(self.pushButtonRemove)
        self.label_2 = QtWidgets.QLabel(Addpath)
        self.label_2.setGeometry(QtCore.QRect(390, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(Addpath)
        self.widget.setGeometry(QtCore.QRect(40, 270, 111, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonMtoT = QtWidgets.QPushButton(self.widget)
        self.pushButtonMtoT.setObjectName("pushButtonMtoT")
        self.verticalLayout.addWidget(self.pushButtonMtoT)
        self.pushButtonMU = QtWidgets.QPushButton(self.widget)
        self.pushButtonMU.setObjectName("pushButtonMU")
        self.verticalLayout.addWidget(self.pushButtonMU)
        self.pushButtonMD = QtWidgets.QPushButton(self.widget)
        self.pushButtonMD.setObjectName("pushButtonMD")
        self.verticalLayout.addWidget(self.pushButtonMD)
        self.pushButtonMtoB = QtWidgets.QPushButton(self.widget)
        self.pushButtonMtoB.setObjectName("pushButtonMtoB")
        self.verticalLayout.addWidget(self.pushButtonMtoB)
        self.pushButtonSave = QtWidgets.QPushButton(Addpath)
        self.pushButtonSave.setGeometry(QtCore.QRect(420, 470, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setObjectName("pushButtonSave")

        self.retranslateUi(Addpath)
        QtCore.QMetaObject.connectSlotsByName(Addpath)

    def retranslateUi(self, Addpath):
        Addpath.setWindowTitle(QtWidgets.QApplication.translate("Addpath", "Add Path", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Addpath", "Notice: Search Priority is defined by Folder Order!", None, -1))
        self.pushButtonAF.setText(QtWidgets.QApplication.translate("Addpath", "Add Folder", None, -1))
        self.pushButtonRemove.setText(QtWidgets.QApplication.translate("Addpath", "Remove", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Addpath", "Media Path", None, -1))
        self.pushButtonMtoT.setText(QtWidgets.QApplication.translate("Addpath", "Move to Top", None, -1))
        self.pushButtonMU.setText(QtWidgets.QApplication.translate("Addpath", "Move Up", None, -1))
        self.pushButtonMD.setText(QtWidgets.QApplication.translate("Addpath", "Move Down", None, -1))
        self.pushButtonMtoB.setText(QtWidgets.QApplication.translate("Addpath", "Move to Bottom", None, -1))
        self.pushButtonSave.setText(QtWidgets.QApplication.translate("Addpath", "Save", None, -1))

