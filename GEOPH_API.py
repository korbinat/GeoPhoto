from PyQt5 import QtWidgets, QtGui, QtCore, QtSql
from PyQt5.QtGui import QPixmap
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS, GPSTAGS
import sys
import os
import re
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QInputDialog, QPushButton, QApplication
from PyQt5.QtWidgets import QFileDialog, QLineEdit, QRadioButton, QButtonGroup
import requests
from requests import get
from geo_api_1 import Ui_MainWindow, examplePopup, ExamplePopup, Example





class mywindow(QtWidgets.QMainWindow, QtWidgets.QWidget):
    def __init__(self):
        super(mywindow, self).__init__()
        self.sOldFileNAme = ""
        self.sNewFileNAme = self.sOldFileNAme
        self.sSuffix = ""
        self.sPath = "" 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonDir.clicked.connect(self.pushButtonDirClick)
        self.ui.pushButton1.clicked.connect(self.pushButton1_clicked)
        self.fileModel = QtWidgets.QFileSystemModel(self)
        self.fileModel.setReadOnly(False)
        self.fileModel.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Files)
        absoluteFilePath = os.path.abspath(__file__)
        self.path_dir = os.path.split(absoluteFilePath)[0]
        path_ = open('path.txt', encoding="utf-8")
        path = path_.readlines()[0]
        path_.close()
        self.fileModel.setRootPath(path)
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
        self.setWindowIcon(QtGui.QIcon("пиктограмма1.png"))
        self.flag1 = False
        self.flag2 = False
        self.flag3 = False
        self.ui.checkBox04.stateChanged.connect(self.click04)
        self.ui.checkBox6_10.stateChanged.connect(self.click6_10)
        self.ui.checkBox110.stateChanged.connect(self.click110)
        self.ui.action.triggered.connect(self.click)
        self.ui.action_2.triggered.connect(self.bbttnn)
        self.ui.action_3.triggered.connect(self.btn3)
        self.ui.group.buttonClicked.connect(self._on_radio_button_clicked)
        self.map_type = "sat,skl"
    
    def _on_radio_button_clicked(self, button):
        if "Схема" == button.text():
            self.map_type = "map"
        elif "Спутниk" in button.text():
            self.map_type = "sat"
        else:
            self.map_type = "sat,skl"
    
    
    def bbttnn(self):
        self.exPopup = examplePopup("""Программа Фёдора Архипенкова
Созданая в 2020-2021 году
В качестве проекта в яндекс лицее""")
        self.exPopup.setGeometry(500, 500, 185, 50)
        self.exPopup.setWindowTitle("Информация")
        self.exPopup.show()

    def click04(self, state):
        if state == QtCore.Qt.Checked:
            self.flag1 = True
        else:
            self.flag1 = False
    
    def click6_10(self, state):
        if state == QtCore.Qt.Checked:
            self.flag2 = True
        else:
            self.flag2 = False
    
    def click110(self, state):
        if state == QtCore.Qt.Checked:
            self.flag3 = True
        else:
            self.flag3 = False
    
    def btn3(self):
        font = QtWidgets.QFontDialog.getFont()
        self.ui.rbtn1.setFont(font[0])
        self.ui.rbtn2.setFont(font[0])
        self.ui.rbtn3.setFont(font[0])
        self.ui.lbl2.setFont(font[0])
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
                os.rename(self.ui.lineEditTo.text(), self.ui.lineEditFrom.text().lower())

    def tableWidget_clicked(self):
        self.sNewFileNAme = ""
        t = ""
        for item in self.ui.tableWidget.selectedItems():
            t = re.sub('[^-a-zA-Zа-яА-Я0-9_.() ]+', '', item.text()) + " "
            self.sNewFileNAme += t
        self.ui.lineEditFrom.setText(self.sPath + '/' +
                                       self.sNewFileNAme + '.' + self.sSuffix)
        self.makeNewName()

    def makeNewName(self):
        if self.sSuffix.upper() in ['JPG', 'JPEG', 'PNG']:
            self.ui.lineEditTo.setText(self.sPath + '/' +
                                       self.sOldFileNAme)
        else:
            self.ui.lineEditTo.setText("")
        
    def get_distance(self, GPSLongitude, GPSLatitude, mDistance=100):
            voltage = "'200 кВ'"
            if self.flag1:
                voltage += ", '0,4 кВ', '0,23 кВ', '0,22 кВ', '0,38 кВ'"
            if self.flag1 and self.flag2:
                voltage += ", '0,4 кВ', '0,23 кВ', '0,22 кВ', '0,38 кВ'"
                voltage += ", '6 кВ', '10 кВ', '20 кВ', '35 кВ'"
            if self.flag1 and self.flag2 and self.flag3:
                voltage += ", '0,4 кВ', '0,23 кВ', '0,22 кВ', '0,38 кВ'"
                voltage += ", '6 кВ', '10 кВ', '20 кВ', '35 кВ', '110 кВ'"
            if self.flag1 and self.flag3:
                voltage += ", '0,4 кВ', '0,23 кВ', '0,22 кВ', '0,38 кВ', '110 кВ'"
            if self.flag3:
                voltage += ", '110 кВ'"
            if self.flag2:
                voltage += ", '6 кВ', '10 кВ', '20 кВ', '35 кВ'"
            if self.flag2 and self.flag3:
                voltage += ", '6 кВ', '10 кВ', '20 кВ', '35 кВ', '110 кВ'"
            self.table = []
            cntrow = 0
            self.ui.tableWidget.clear()
            coordinates = []
            float_coordinates = []
            #lst = sorted(get(f"http://localhost:5000/api/geo/{GPSLongitude}/{GPSLatitude}/{voltage}/{self.ui.spinBox_2.value()}/{mDistance}").json(),
            lst = sorted(get(f"https://flasktest.spin-one.ru/api/geo/{GPSLongitude}/{GPSLatitude}/{voltage}/{self.ui.spinBox_2.value()}/{mDistance}").json(),
                             key=lambda x: x["DIST"])[:self.ui.spinBox_2.value()]
            lst_ = []
            for i in lst:
                lst_.append([])
                lst_[-1].append(i['DIST'])
                lst_[-1].append(i['TYPETM'])
                lst_[-1].append(i['NAMETM'])
                lst_[-1].append(i['KLASSVOLTAGE'])
                lst_[-1].append(i['PARTVL'])
                lst_[-1].append(i['NAMEVL'])
                lst_[-1].append(i['MANAGE'])
                lst_[-1].append(i['DIVISION'])
                lst_[-1].append(i['POINT'])
            for row in lst_:
                row_ = row[-1].replace("POINT(", "").replace(")", "").replace(" ", ",") + ",flag"
                coordinates.append(f"~" + row_)
                self.ui.tableWidget.setItem(cntrow, 0, QtWidgets.QTableWidgetItem(
                    '{0:.2f} м.'.format(row[0])))
                row__ = row[-1].replace("POINT(", "").replace(")", "").split()
                float_coordinates.append(list(map(float, row__)))
                self.ui.tableWidget.setItem(cntrow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.ui.tableWidget.setItem(cntrow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.ui.tableWidget.setItem(cntrow, 3, QtWidgets.QTableWidgetItem(row[3]))
                self.ui.tableWidget.setItem(cntrow, 4, QtWidgets.QTableWidgetItem(row[4]))
                self.ui.tableWidget.setItem(cntrow, 5, QtWidgets.QTableWidgetItem(row[5]))
                self.ui.tableWidget.setItem(cntrow, 6, QtWidgets.QTableWidgetItem(row[6]))
                self.ui.tableWidget.setItem(cntrow, 7, QtWidgets.QTableWidgetItem(row[7]))
                self.table.append(list(row))
                cntrow += 1
            self.ui.tableWidget.setHorizontalHeaderLabels(('Дистанция', 'Тип',
                                                           'Наименование', 'Класс U',
                                                           'Часть ВЛ', 'Наименование ВЛ',
                                                           'Управляется', 'Подразделение'))
            return [coordinates[:self.ui.spinBox_2.value()],
                    float_coordinates[:self.ui.spinBox_2.value()]]

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
        degrees = dms[0]  # degrees = dms[0][0] / dms[0][1]
        minutes = dms[1] / 60.0  # minutes = dms[1][0] / dms[1][1] / 60.0
        seconds = dms[2] / 3600.0  # seconds = dms[2][0] / dms[2][1] / 3600.0
        if ref in ['S', 'W']:
            degrees = -degrees
            minutes = -minutes
            seconds = -seconds
        return round(degrees + minutes + seconds, 5)

    def listViewClick(self):
        if len(str(self.ui.spinBox_2.value())) > 0:
            row = self.ui.spinBox_2.value()
            self.ui.tableWidget.setRowCount(row)
        self.sNewFileNAme = self.sOldFileNAme
        for ix in self.ui.listView.selectedIndexes():
            file_ = self.fileModel.fileInfo(ix)
            self.sOldFileNAme = file_.fileName()
            self.ui.lineEditFrom.setText(file_.absoluteFilePath())
            self.sSuffix = file_.suffix()
            self.sPath = file_.canonicalPath()
            self.makeNewName()

            if str(file_.suffix()).upper() in ['JPG', 'JPEG', 'PNG']:
                geot = self.get_geotagging(file_.absoluteFilePath())
                if len(geot):
                    fLatitude = self.get_decimal_from_dms(geot['GPSLatitude'],
                                                          geot['GPSLatitudeRef'])
                    fLongitude = self.get_decimal_from_dms(geot['GPSLongitude'],
                                                           geot['GPSLongitudeRef'])
                    pixmap = QtGui.QPixmap(file_.absoluteFilePath())
                    scaled = pixmap.scaled(self.ui.label_2.size(), QtCore.Qt.KeepAspectRatio)
                    self.ui.label_2.setPixmap(scaled)
                    self.ui.label.setText(f'{str(fLatitude)}\n{str(fLongitude)}')
                    intt = 50
                    if len(str(self.ui.spinBox.value())) > 0:
                        intt = self.ui.spinBox.value()
                    coordinates = self.get_distance(fLongitude,
                                                         fLatitude, intt)
                    coordinates, float_coordinates = coordinates
                    try:
                        max_coordinate_1 = max(float_coordinates, key=lambda x: float(x[0]))[0]
                        min_coordinate_1 = min(float_coordinates, key=lambda x: float(x[0]))[0]
                        max_coordinate_2 = max(float_coordinates, key=lambda x: float(x[1]))[1]
                        min_coordinate_2 = min(float_coordinates, key=lambda x: float(x[1]))[1]
                        coords = max([max_coordinate_1 - min_coordinate_1,
                                      max_coordinate_2 - min_coordinate_2]) + 0.0005
                    except Exception:
                        coords = 0.0005
                    http = 'http://static-maps.yandex.ru/1.x/?ll='
                    map_request = f"{http}{fLongitude},{fLatitude}&spn={coords}"
                    map_request += f",{coords}&l={self.map_type}&pt={','.join(coordinates)[1:]}"
                    response = requests.get(map_request)
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
                    self.pixmap = QPixmap(map_file)
                    self.ui.lbl.setPixmap(self.pixmap)
                else:
                    self.ui.label.setText('Нет геоданных')

    def pushButtonDirClick(self):
        options = QtWidgets.QFileDialog.Options()
        options = QtWidgets.QFileDialog.DontUseNativeDialog
        path_ = open('path.txt', encoding="utf-8")
        path = path_.readlines()
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


app = QtWidgets.QApplication([])
win = mywindow()
win.show()
sys.exit(app.exec())