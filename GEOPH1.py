from PyQt5 import QtWidgets, QtGui, QtCore, QtSql
from PyQt5.QtGui import QPixmap
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS, GPSTAGS
import sys
import os
import re
import sqlite3
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QInputDialog, QPushButton, QFileDialog, QLineEdit, QRadioButton, QButtonGroup
import requests
#import spatialite


class examplePopup(QWidget):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.initUI()

    def initUI(self):
        lblName = QLabel(self.name, self)


class ExamplePopup(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.le = QLineEdit(self)
        self.le.resize(150, 20)
        self.le.move(10, 10)
        self.le2 = QLineEdit(self)
        self.le2.resize(150, 20)
        self.le2.move(10, 30)
        self.le3 = QLineEdit(self)
        self.le3.resize(150, 20)
        self.le3.move(10, 50)
        self.le4 = QLineEdit(self)
        self.le4.resize(150, 20)
        self.le4.move(10, 70)
        self.le5 = QLineEdit(self)
        self.le5.resize(150, 20)
        self.le5.move(10, 90)
        self.le6 = QLineEdit(self)
        self.le6.resize(150, 20)
        self.le6.move(10, 110)
        self.le7 = QLineEdit(self)
        self.le7.resize(150, 20)
        self.le7.move(10, 130)
        self.le8 = QLineEdit(self)
        self.le8.resize(150, 20)
        self.le8.move(10, 150)
        self.le9 = QLineEdit(self)
        self.le9.resize(150, 20)
        self.le9.move(10, 170)
        self.le10 = QLineEdit(self)
        self.le10.resize(150, 20)
        self.le10.move(10, 190)
        self.le.setText("ID")
        self.le2.setText("NAMETM")
        self.le3.setText("DIVISION")
        self.le4.setText("IKLASSVOLTAGED")
        self.le5.setText("PARTVL")
        self.le6.setText("NAMEVL")
        self.le7.setText("MANAGE")
        self.le8.setText("TYPETM")
        self.le9.setText("DATEEDIT")
        self.le10.setText("KODTM")
        self.btn = QPushButton(self)
        self.btn.resize(100, 20)
        self.btn.move(10, 230)
        self.btn.setText("Добавить")


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.x = 0
        self.setGeometry(300, 300, 700, 700)
        self.setWindowTitle('Фокусы с арифметикой')
        self.lbl = QLabel(self)
        self.lbl.move(50, 35)
        self.lbl.resize(600, 600)
        self.lbl1 = QLabel(self)
        self.lbl1.resize(1000, 20)
        self.lbl1.move(0, 20)
        self.btn = QPushButton(self)
        self.btn.move(20, 0)
        self.btn.resize(20, 20)
        self.btn.setText("->")
        self.btn.clicked.connect(self.run)
        self.btn1 = QPushButton(self)
        self.btn1.resize(20, 20)
        self.btn1.setText("<-")
        self.btn1.clicked.connect(self.run)
        self.lst = []
        self.lst1 = ["Указать файл db",
                     "Выбор изображения",
                     "Указать директорию изображений",
                     "Выбрать силу тока показываемых опор",
                     "Из таблицы ближайших опор надо указать то как вы хотите назвать свою опору, нажать кнопку “переименовать”",
                     "Так же можно указать до какого расстояния будет показываться опоры, сколько будет показываться ближайших опор."]
        for i in range(1, 7):
            self.lst.append(f"Фото{str(i)}.jpg")
        self.lbl.setPixmap(QPixmap(self.lst[self.x]))
        self.lbl1.setText(self.lst1[self.x])
        
    def run(self):
        if self.x < 5 and self.sender().text() == "->":
            self.x += 1
        if self.x > 0 and self.sender().text() == "<-":
            self.x -= 1
        self.lbl.setPixmap(QPixmap(self.lst[self.x]))
        self.lbl1.setText(self.lst1[self.x])


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 826)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonDir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDir.setGeometry(QtCore.QRect(10, 10, 181, 33))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButtonDir.setFont(font)
        self.pushButtonDir.setObjectName("pushButtonDir")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 40, 261, 631))
        self.listView.setObjectName("listView")
        self.group = QButtonGroup(self.centralwidget)
        self.group.setObjectName("group")
        self.rbtn1 = QRadioButton(self.centralwidget)
        self.rbtn1.setText("Схема")
        self.group.addButton(self.rbtn1)
        self.rbtn1.move(750, 370)
        self.rbtn1.setObjectName("rbtn1")
        self.rbtn2 = QRadioButton(self.centralwidget)
        self.rbtn2.setText("Спутниk")
        self.group.addButton(self.rbtn2)
        self.rbtn2.move(830, 370)
        self.rbtn2.setObjectName("rbtn2")
        self.rbtn3 = QRadioButton(self.centralwidget)
        self.rbtn3.setText("Гибрид")
        self.group.addButton(self.rbtn3)
        self.rbtn3.move(925, 370)
        self.rbtn3.setObjectName("rbtn3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 40, 391, 31))
        self.label.setText("")
        self.label.setScaledContents(False)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(750, 20, 351, 351))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setLineWidth(1)
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.lb = QtWidgets.QLabel(self.centralwidget)
        self.lb.setGeometry(QtCore.QRect(750, 400, 351, 351))
        self.lb.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lb.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lb.setLineWidth(1)
        self.lb.setText("")
        self.lb.setScaledContents(True)
        self.lb.setObjectName("lb")
        self.lb2 = QtWidgets.QLabel(self.centralwidget)
        self.lb2.setGeometry(QtCore.QRect(1000, 369, 70, 20))
        self.lb2.setLineWidth(1)
        self.lb2.setText("Карта")
        self.lb2.setScaledContents(True)
        self.lb2.setObjectName("lb2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(280, 380, 416, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.lineEditTo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTo.setGeometry(QtCore.QRect(10, 704, 701, 20))
        self.lineEditTo.setObjectName("lineEditTo")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(480, 74, 100, 20))
        self.pushButton3.setText("Сменить путь")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(10, 750, 121, 33))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        self.lineEditFrom = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFrom.setGeometry(QtCore.QRect(10, 680, 701, 20))
        self.lineEditFrom.setObjectName("lineEditFrom")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 100, 431, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 200, 111, 31))
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(280, 150, 91, 31))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(999999)
        self.spinBox.setProperty("value", 100)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(280, 240, 51, 31))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setProperty("value", 15)
        self.spinBox_2.setObjectName("spinBox_2")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox6_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox6_10.setGeometry(QtCore.QRect(280, 330, 121, 20))
        self.checkBox6_10.setObjectName("checkBox6_10")
        self.checkBox04 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox04.setGeometry(QtCore.QRect(280, 310, 121, 17))
        self.checkBox04.setObjectName("checkBox04")
        self.checkBox110 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox110.setGeometry(QtCore.QRect(280, 350, 70, 17))
        self.checkBox110.setObjectName("checkBox110")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 280, 191, 20))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.action_4)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ГЕОФото"))
        self.pushButtonDir.setText(_translate("MainWindow", "Выберите директорию"))
        self.pushButton1.setText(_translate("MainWindow", "Смена имени"))
        self.label_3.setText(_translate("MainWindow", "Введите максимальное растояние(1-999999 в метрах)"))
        self.label_4.setText(_translate("MainWindow", "Показать опор(1-99)"))
        self.checkBox6_10.setText(_translate("MainWindow", "6-10-20-35"))
        self.checkBox04.setText(_translate("MainWindow", "0,4-0,22-0,23,0,38"))
        self.checkBox110.setText(_translate("MainWindow", "110"))
        self.label_5.setText(_translate("MainWindow", "Искать по уровню напряжения"))
        self.menu.setTitle(_translate("MainWindow", "Помощь"))
        self.menu_2.setTitle(_translate("MainWindow", "Бонус"))
        self.action.setText(_translate("MainWindow", "О программе"))
        self.action_2.setText(_translate("MainWindow", "О создателе"))
        self.action_3.setText(_translate("MainWindow", "Шрифт"))
        self.action_4.setText(_translate("MainWindow", "Добавить опору"))


class mywindow(QtWidgets.QMainWindow, QtWidgets.QWidget):
    def __init__(self):
        super(mywindow, self).__init__()
        self.sOldFileNAme = ""
        self.sNewFileNAme = "НОВОЕ ИМЯ "
        self.sSuffix = ""
        self.sPath = "" 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonDir.clicked.connect(self.pushButtonDirClick)
        self.ui.pushButton1.clicked.connect(self.pushButton1_clicked)
        path = r'D:\Users\komi0645\Documents\PY\python\geoPh\SOURCE'
        self.fileModel = QtWidgets.QFileSystemModel(self)
        self.fileModel.setReadOnly(False)
        self.fileModel.setRootPath(path)
        self.fileModel.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Files)
        self.ui.listView.setModel(self.fileModel)
        self.ui.listView.setRootIndex(self.fileModel.index(path))
        self.ui.listView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.ui.listView.clicked.connect(self.listViewClick)
        self.ui.tableWidget.setColumnCount(8)
        row = 10
        self.ui.tableWidget.setRowCount(row)
        self.ui.tableWidget.setHorizontalHeaderLabels(('Дистанция', 'Тип',
                                                       'Наименование', 'Класс U',
                                                       'Часть ВЛ', 'Наименование ВЛ',
                                                       'Управляется', 'Подразделение'))
        self.ui.tableWidget.itemClicked.connect(self.tableWidget_clicked)
        self.createConnection("db1.sqlite")
        
        self.ui.lineEditFrom.setReadOnly(True)
        self.setWindowIcon(QtGui.QIcon("пиктограмма1.png"))
        self.f1 = False
        self.f2 = False
        self.f3 = False
        self.ui.checkBox04.stateChanged.connect(self.click04)
        self.ui.checkBox6_10.stateChanged.connect(self.click6_10)
        self.ui.checkBox110.stateChanged.connect(self.click110)
        self.ui.pushButton3.clicked.connect(self.click77)
        self.ui.action.triggered.connect(self.click)
        self.ui.action_2.triggered.connect(self.bbttnn)
        self.ui.action_3.triggered.connect(self.btn3)
        self.ui.action_4.triggered.connect(self.click321)
        self.ui.tableWidget.cellChanged.connect(self.change)
        self.ui.group.buttonClicked.connect(self._on_radio_button_clicked)
        self.map_type = "map"
    
    def _on_radio_button_clicked(self, button):
        if "Схема" == button.text():
            self.map_type = "map"
        elif "Спутниk" in button.text():
            self.map_type = "sat"
        else:
            self.map_type = "sat,skl"
    def change(self, row, column):
        try:
            for item in self.ui.tableWidget.selectedItems():
                print(self.table[row])
                self.table[row][column] = item.text()
                print(self.table[row])
                t = self.table[row]
                zapros = f"""UPDATE TECHPLACE
                SET TYPETM = '{t[1]}', NAMETM = '{t[2]}', KLASSVOLTAGE = '{t[3]}'
                , PARTVL = '{t[4]}', NAMEVL = '{t[5]}', MANAGE = '{t[6]}', DIVISION = '{t[7]}'
                WHERE ID = {t[8]}"""
                print(zapros)
                self.curr.execute(zapros)
                self.db.commit()
        except Exception:
            pass
    
    def click77(self):
        try:
            self.createConnection(QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.sqlite);;Картинка (*.sqlite);;Все файлы (*)'))[0]
        except Exception:
            self.createConnection("db1.sqlite")
    
    def createConnection(self, namefiledb="db1.sqlite"):
        # Создаю соединение с базой данных координат опор
        self.db = sqlite3.connect(namefiledb)
        self.db.enable_load_extension(True)
        self.db.load_extension('mod_spatialite')
        self.curr = self.db.cursor()
        self.statusBar().showMessage(f"Вы работаете с {namefiledb}")
    
    def bbttnn(self):
        self.exPopup = examplePopup("""Программа Фёдора Архипенкова
Созданая в 2020 году
В качестве проекта в яндекс лицее""")
        self.exPopup.setGeometry(500, 500, 185, 50)
        self.exPopup.setWindowTitle("Информация")
        self.exPopup.show()

    def click04(self, state):
        if state == QtCore.Qt.Checked:
            self.f1 = True
        else:
            self.f1 = False
    
    def click6_10(self, state):
        if state == QtCore.Qt.Checked:
            self.f2 = True
        else:
            self.f2 = False
    
    def click110(self, state):
        if state == QtCore.Qt.Checked:
            self.f3 = True
        else:
            self.f3 = False
    
    def btn3(self):
        font = QtWidgets.QFontDialog.getFont()
        self.ui.rbtn1.setFont(font[0])
        self.ui.rbtn2.setFont(font[0])
        self.ui.rbtn3.setFont(font[0])
        self.ui.lb2.setFont(font[0])
        self.ui.spinBox.setFont(font[0])
        self.ui.spinBox_2.setFont(font[0])
        self.ui.label.setFont(font[0])
        self.ui.label_2.setFont(font[0])
        self.ui.label_3.setFont(font[0])
        self.ui.label_4.setFont(font[0])
        self.ui.label_5.setFont(font[0])
        self.ui.lineEditFrom.setFont(font[0])
        self.ui.lineEditTo.setFont(font[0])
        self.ui.listView.setFont(font[0])
        self.ui.menubar.setFont(font[0])
        self.ui.statusbar.setFont(font[0])
        self.ui.tableWidget.setFont(font[0])
        self.ui.checkBox04.setFont(font[0])
        self.ui.checkBox110.setFont(font[0])
        self.ui.checkBox6_10.setFont(font[0])

    def pushButton1_clicked(self):
        reply = QtWidgets.QMessageBox.question(self, "Ответьте на вопрос", "хотите переименовать?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            if len(self.ui.lineEditTo.text()) != 0:
                os.rename(self.ui.lineEditFrom.text(), self.ui.lineEditTo.text())

    def tableWidget_clicked(self):
        self.sNewFileNAme = ""
        t = ""
        for item in self.ui.tableWidget.selectedItems():
            t = re.sub('[^-a-zA-Zа-яА-Я0-9_.() ]+', '', item.text()) + " "
            self.sNewFileNAme += t
        self.makeNewName()

    def makeNewName(self):
        if self.sSuffix.upper() in ['JPG', 'JPEG', 'PNG']:
            self.ui.lineEditTo.setText(self.sPath + '/' +
                                       self.sNewFileNAme[:-1] + '.' + self.sSuffix)
        else:
            self.ui.lineEditTo.setText("")
        
    def get_distance(self, GPSLongitude, GPSLatitude, mDistance=100):
        try:
            qwe = ""
            if self.f1:
                qwe = ", '0,4 кВ', '0,23 кВ', '0,22 кВ', '0,38 кВ'"
            if self.f1 and self.f2:
                qwe = ", '0,4 кВ', '0,23 кВ', '0,22 кВ', '0,38 кВ', '6 кВ', '10 кВ', '20 кВ', '35 кВ'"
            if self.f1 and self.f2 and self.f3:
                qwe = ", '0,4 кВ', '0,23 кВ', '0,22 кВ', '0,38 кВ'"
                qwe += ", '6 кВ', '10 кВ', '20 кВ', '35 кВ', '110 кВ'"
            if self.f1 and self.f3:
                qwe = ", '0,4 кВ', '0,23 кВ', '0,22 кВ', '0,38 кВ', '110 кВ'"
            if self.f3:
                qwe = ", '110 кВ'"
            if self.f2:
                qwe = ", '6 кВ', '10 кВ', '20 кВ', '35 кВ'"
            if self.f2 and self.f3:
                qwe = ", '6 кВ', '10 кВ', '20 кВ', '35 кВ', '110 кВ'"
            strsql = f'''select Distance(GeomFromText('POINT ({str(GPSLongitude)} {str(GPSLatitude)})', 4326), GEOMETRYPLACE, 1)
            AS DIST, TYPETM, NAMETM, KLASSVOLTAGE, PARTVL, NAMEVL, MANAGE, DIVISION, ID
            from TECHPLACE where KLASSVOLTAGE IN('220 кВ'{qwe}) and PtDistWithin(GeomFromText
            ('POINT ({str(GPSLongitude)} {str(GPSLatitude)})', 4326),GEOMETRYPLACE , {mDistance},1)'''
            self.table = []
            cntrow = 0
            self.ui.tableWidget.clear()
            for row in self.curr.execute(strsql):
                self.ui.tableWidget.setItem(cntrow, 0, QtWidgets.QTableWidgetItem(
                    '{0:.2f} м.'.format(row[0])))
                self.ui.tableWidget.setItem(cntrow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.ui.tableWidget.setItem(cntrow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.ui.tableWidget.setItem(cntrow, 3, QtWidgets.QTableWidgetItem(row[3]))
                self.ui.tableWidget.setItem(cntrow, 4, QtWidgets.QTableWidgetItem(row[4]))
                self.ui.tableWidget.setItem(cntrow, 5, QtWidgets.QTableWidgetItem(row[5]))
                self.ui.tableWidget.setItem(cntrow, 6, QtWidgets.QTableWidgetItem(row[6]))
                self.ui.tableWidget.setItem(cntrow, 7, QtWidgets.QTableWidgetItem(row[7]))
                self.table.append(list(row))
                cntrow += 1
        except Exception (IndexError, ValueError):
            pass
            #print(IndexError, ValueError)

    def get_geotagging(self, filename):
        image = Image.open(filename)
        exif = image._getexif()
        geotagging = {}
        if exif:
            for (idx, tag) in TAGS.items():
                if tag == 'GPSInfo':
                    if idx not in exif:
                        raise ValueError("No EXIF geotagging found")
                    for (key, val) in GPSTAGS.items():
                        if key in exif[idx]:
                            geotagging[val] = exif[idx][key]
        return geotagging

    def get_decimal_from_dms(self, dms, ref):
        #degrees = dms[0][0] / dms[0][1]
        #minutes = dms[1][0] / dms[1][1] / 60.0
        #seconds = dms[2][0] / dms[2][1] / 3600.0
        degrees = dms[0]
        minutes = dms[1] / 60.0
        seconds = dms[2] / 3600.0
        if ref in ['S', 'W']:
            degrees = -degrees
            minutes = -minutes
            seconds = -seconds
        return round(degrees + minutes + seconds, 5)

    def listViewClick(self):
        if len(str(self.ui.spinBox_2.value())) > 0:
            row = self.ui.spinBox_2.value()
            self.ui.tableWidget.setRowCount(row)
        self.sNewFileNAme = "НОВОЕ ИМЯ "
        for ix in self.ui.listView.selectedIndexes():
            f = self.fileModel.fileInfo(ix)
            self.sOldFileNAme = f.fileName()
            self.ui.lineEditFrom.setText(f.absoluteFilePath())
            self.sSuffix = f.suffix()
            self.sPath = f.canonicalPath()
            self.makeNewName()

            if str(f.suffix()).upper() in ['JPG', 'JPEG', 'PNG']:
                geot = self.get_geotagging(f.absoluteFilePath())
                if len(geot):
                    fLatitude = self.get_decimal_from_dms(geot['GPSLatitude'],
                                                          geot['GPSLatitudeRef'])
                    fLongitude = self.get_decimal_from_dms(geot['GPSLongitude'],
                                                           geot['GPSLongitudeRef'])
                    map_request = f"http://static-maps.yandex.ru/1.x/?ll={fLongitude},{fLatitude}&spn=0.0005,0.0005&l={self.map_type}"
                    response = requests.get(map_request)
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
                    self.pixmap = QPixmap(map_file)
                    self.ui.lb.setPixmap(self.pixmap)
                    pixmap = QtGui.QPixmap(f.absoluteFilePath())
                    scaled = pixmap.scaled(self.ui.label_2.size(), QtCore.Qt.KeepAspectRatio)
                    self.ui.label_2.setPixmap(scaled)
                    self.ui.label.setText(f'{str(fLatitude)}\n{str(fLongitude)}')
                    intt = 50
                    if len(str(self.ui.spinBox.value())) > 0:
                        intt = self.ui.spinBox.value()
                    self.get_distance(str(fLongitude), str(fLatitude), intt)
                else:
                    self.ui.label.setText('Нет геоданных')

    def pushButtonDirClick(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        path_ = open('path.txt', encoding="utf-8")
        path = path_.readlines()
        print(path)
        direct = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                            "Выберите папку с фотографиями",
                                                            directory=path[0],
                                                            options=options)
        if direct:
            path_ = open('path.txt', "w", encoding="utf-8")
            path_.write(direct)
            self.fileModel = QtWidgets.QFileSystemModel(self)
            self.fileModel.setRootPath(direct)
            self.fileModel.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Files)
            self.ui.listView.setModel(self.fileModel)
            self.ui.listView.setRootIndex(self.fileModel.index(direct))
    
    def click(self):
        self.exPopup = Example()
        self.exPopup.setGeometry(500, 500, 700, 700)
        self.exPopup.setWindowTitle("Информация")
        self.exPopup.show()
    
    def click321(self):
        self.exPopup1 = ExamplePopup()
        self.exPopup1.setGeometry(500, 500, 225, 500)
        self.exPopup1.setWindowTitle("Добавление")
        self.exPopup1.btn.clicked.connect(self.click1234)
        self.exPopup1.show()
    
    def click1234(self):
        try:
            lst = [self.exPopup1.le.text(),
            self.exPopup1.le2.text(),
            self.exPopup1.le3.text(),
            self.exPopup1.le4.text(),
            self.exPopup1.le5.text(),
            self.exPopup1.le6.text(),
            self.exPopup1.le7.text(),
            self.exPopup1.le8.text(),
            self.exPopup1.le9.text(),
            self.exPopup1.le10.text()
            ]
            zapros = f"""INSERT INTO TECHPLACE(ID, NAMETM, DIVISION
            , KLASSVOLTAGE, PARTVL, NAMEVL, MANAGE, TYPETM, DATEEDIT, KODTM)
            VALUES({lst[0]}, '{lst[1]}', '{lst[2]}', '{lst[3]}', '{lst[4]}'
            , '{lst[5]}', '{lst[6]}', '{lst[7]}', '{lst[8]}', '{lst[9]}')"""
            print(zapros)
            self.curr.execute(zapros)
            self.db.commit()
            self.exPopup1.close()
        except Exception:
            pass


app = QtWidgets.QApplication([])
win = mywindow()
win.show()
sys.exit(app.exec())