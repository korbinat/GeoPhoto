# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'geo_api_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1107, 903)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonDir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDir.setMinimumSize(QtCore.QSize(150, 31))
        self.pushButtonDir.setMaximumSize(QtCore.QSize(150, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonDir.setFont(font)
        self.pushButtonDir.setObjectName("pushButtonDir")
        self.verticalLayout.addWidget(self.pushButtonDir)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setMinimumSize(QtCore.QSize(300, 0))
        self.listView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(80, 31))
        self.label.setMaximumSize(QtCore.QSize(16777215, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(300, 31))
        self.label_3.setMaximumSize(QtCore.QSize(300, 36))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setMinimumSize(QtCore.QSize(91, 31))
        self.spinBox.setMinimum(100)
        self.spinBox.setMaximum(6999)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_5.addWidget(self.spinBox)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(130, 31))
        self.label_4.setMaximumSize(QtCore.QSize(130, 36))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setMinimumSize(QtCore.QSize(51, 31))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setSingleStep(1)
        self.spinBox_2.setProperty("value", 15)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_5.addWidget(self.spinBox_2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMinimumSize(QtCore.QSize(160, 31))
        self.label_5.setMaximumSize(QtCore.QSize(160, 36))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.checkBox04 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox04.setObjectName("checkBox04")
        self.verticalLayout_5.addWidget(self.checkBox04)
        self.checkBox6_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox6_10.setObjectName("checkBox6_10")
        self.verticalLayout_5.addWidget(self.checkBox6_10)
        self.checkBox110 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox110.setObjectName("checkBox110")
        self.verticalLayout_5.addWidget(self.checkBox110)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(416, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lbl = QtWidgets.QLabel(self.centralwidget)
        self.lbl.setMinimumSize(QtCore.QSize(351, 351))
        self.lbl.setObjectName("lbl")
        self.gridLayout_3.addWidget(self.lbl, 2, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.group = QtWidgets.QButtonGroup(self.centralwidget)
        self.group.setObjectName("group")
        self.rbtn1 = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn1.setMinimumSize(QtCore.QSize(80, 31))
        self.rbtn1.setMaximumSize(QtCore.QSize(80, 31))
        self.rbtn1.setObjectName("rbtn1")
        self.group.addButton(self.rbtn1)
        self.gridLayout_4.addWidget(self.rbtn1, 0, 0, 1, 1)
        self.rbtn2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn2.setMinimumSize(QtCore.QSize(80, 31))
        self.rbtn2.setMaximumSize(QtCore.QSize(80, 31))
        self.rbtn2.setObjectName("rbtn2")
        self.group.addButton(self.rbtn2)
        self.gridLayout_4.addWidget(self.rbtn2, 0, 1, 1, 1)
        self.rbtn3 = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn3.setMinimumSize(QtCore.QSize(80, 31))
        self.rbtn3.setMaximumSize(QtCore.QSize(80, 31))
        self.rbtn3.setObjectName("rbtn3")
        self.group.addButton(self.rbtn3)
        self.gridLayout_4.addWidget(self.rbtn3, 0, 2, 1, 1)
        self.lbl2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl2.setObjectName("lbl2")
        self.gridLayout_4.addWidget(self.lbl2, 0, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(551, 351))
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditTo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTo.setReadOnly(True)
        self.lineEditTo.setObjectName("lineEditTo")
        self.verticalLayout_2.addWidget(self.lineEditTo)
        self.lineEditFrom = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFrom.setObjectName("lineEditFrom")
        self.verticalLayout_2.addWidget(self.lineEditFrom)
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setMinimumSize(QtCore.QSize(150, 31))
        self.pushButton1.setMaximumSize(QtCore.QSize(160, 36))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        self.verticalLayout_2.addWidget(self.pushButton1)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1107, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonDir.setText(_translate("MainWindow", "Выберите директорию"))
        self.label_3.setText(_translate("MainWindow", "Введите максимальное растояние(1-6999 в метрах)"))
        self.label_4.setText(_translate("MainWindow", "Показать опор(1-99)"))
        self.label_5.setText(_translate("MainWindow", "Искать по уровню напряжения"))
        self.checkBox04.setText(_translate("MainWindow", "0,4-0,22-0,23,0,38"))
        self.checkBox6_10.setText(_translate("MainWindow", "6-10-20-35"))
        self.checkBox110.setText(_translate("MainWindow", "110"))
        self.lbl.setText(_translate("MainWindow", "TextLabel"))
        self.rbtn1.setText(_translate("MainWindow", "Схема"))
        self.rbtn2.setText(_translate("MainWindow", "Спутниk"))
        self.rbtn3.setText(_translate("MainWindow", "Гибрид"))
        self.lbl2.setText(_translate("MainWindow", "Карта"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton1.setText(_translate("MainWindow", "Сменить имя"))
        self.menu.setTitle(_translate("MainWindow", "Помощь"))
        self.menu_2.setTitle(_translate("MainWindow", "Бонус"))
        self.action.setText(_translate("MainWindow", "О программе"))
        self.action_2.setText(_translate("MainWindow", "Про автора"))
        self.action_3.setText(_translate("MainWindow", "Шрифт"))