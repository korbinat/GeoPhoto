# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'geophoto.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 826)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonDir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDir.setGeometry(QtCore.QRect(10, 10, 131, 23))
        self.pushButtonDir.setObjectName("pushButtonDir")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 40, 261, 631))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 40, 391, 31))
        self.label.setScaledContents(False)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 370, 311, 301))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setLineWidth(1)
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(280, 70, 831, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.lineEditTo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTo.setGeometry(QtCore.QRect(10, 704, 1101, 20))
        self.lineEditTo.setObjectName("lineEditTo")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(600, 650, 75, 23))
        self.pushButton1.setObjectName("pushButton1")
        self.lineEditFrom = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFrom.setGeometry(QtCore.QRect(10, 680, 1101, 20))
        self.lineEditFrom.setObjectName("lineEditFrom")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ГЕОФото"))
        self.pushButtonDir.setText(_translate("MainWindow", "Выберите директорию"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton1.setText(_translate("MainWindow", "PushButton"))
