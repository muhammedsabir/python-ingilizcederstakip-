# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list.ui'
#
# Created: Mon Apr 24 03:13:51 2017
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(876, 573)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.listEdit = QtGui.QLineEdit(self.centralwidget)
        self.listEdit.setGeometry(QtCore.QRect(120, 10, 171, 20))
        self.listEdit.setObjectName(_fromUtf8("listEdit"))
        self.listEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.listEdit_2.setGeometry(QtCore.QRect(370, 10, 171, 20))
        self.listEdit_2.setObjectName(_fromUtf8("listEdit_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 10, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.listButtonAra = QtGui.QPushButton(self.centralwidget)
        self.listButtonAra.setGeometry(QtCore.QRect(560, 10, 75, 23))
        self.listButtonAra.setObjectName(_fromUtf8("listButtonAra"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 50, 851, 481))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 481))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 876, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "List Screen", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Ad Soyad", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Telefon", None, QtGui.QApplication.UnicodeUTF8))
        self.listButtonAra.setText(QtGui.QApplication.translate("MainWindow", "Ara", None, QtGui.QApplication.UnicodeUTF8))

