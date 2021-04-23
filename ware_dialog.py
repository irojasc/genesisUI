# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ware_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def loadData(self):
        almacen = [{"cod" : "GN_10000","isbn" : "9788478086085","nombre":"LOS SECRETOS DE LA MENTE MILLONARIA","autor":"T.HARV EKER","editorial":"SIRIO","genero":"CRECIMIENTO PERSONAL","cantidad[STC]":20,"cantidad[STGO]":20},
        {"cod" : "GN_1509","isbn" : "9788497772303","nombre":"EL CABALLERO DE LA ARMADURA OXIDADA","autor":"ROBERT FISHER","editorial":"OBELISCO","genero":"NOVELA","cantidad[STC]":1,"cantidad[STGO]":0}]
        row = 0
        self.ware_table.setRowCount(len(almacen))
        for libro in almacen:
            self.ware_table.setItem(row, 0, QtWidgets.QTableWidgetItem(libro["cod"]))
            self.ware_table.setItem(row, 1, QtWidgets.QTableWidgetItem(libro["isbn"]))
            self.ware_table.setItem(row, 2, QtWidgets.QTableWidgetItem(libro["nombre"]))
            self.ware_table.setItem(row, 3, QtWidgets.QTableWidgetItem(libro["autor"]))
            self.ware_table.setItem(row, 4, QtWidgets.QTableWidgetItem(libro["editorial"]))
            self.ware_table.setItem(row, 5, QtWidgets.QTableWidgetItem(libro["genero"]))
            self.ware_table.setItem(row, 6, QtWidgets.QTableWidgetItem(str(libro["cantidad[STC]"])))
            self.ware_table.setItem(row, 7, QtWidgets.QTableWidgetItem(str(libro["cantidad[STGO]"])))
            row =+ 1

    


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1024, 768)
        Dialog.setFixedSize(1024, 768)
        self.top_frame = QtWidgets.QFrame(Dialog)
        self.top_frame.setGeometry(QtCore.QRect(0, 0, 1024, 100))
        self.top_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.298507 rgba(83, 97, 142, 255), stop:1 rgba(97, 69, 128, 255));")
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.search_box = QtWidgets.QGroupBox(self.top_frame)
        self.search_box.setGeometry(QtCore.QRect(20, 10, 621, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.298507, QtGui.QColor(83, 97, 142))
        gradient.setColorAt(1.0, QtGui.QColor(97, 69, 128))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.298507, QtGui.QColor(83, 97, 142))
        gradient.setColorAt(1.0, QtGui.QColor(97, 69, 128))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.298507, QtGui.QColor(83, 97, 142))
        gradient.setColorAt(1.0, QtGui.QColor(97, 69, 128))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.298507, QtGui.QColor(83, 97, 142))
        gradient.setColorAt(1.0, QtGui.QColor(97, 69, 128))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.298507, QtGui.QColor(83, 97, 142))
        gradient.setColorAt(1.0, QtGui.QColor(97, 69, 128))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.298507, QtGui.QColor(83, 97, 142))
        gradient.setColorAt(1.0, QtGui.QColor(97, 69, 128))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.298507, QtGui.QColor(83, 97, 142))
        gradient.setColorAt(1.0, QtGui.QColor(97, 69, 128))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.298507, QtGui.QColor(83, 97, 142))
        gradient.setColorAt(1.0, QtGui.QColor(97, 69, 128))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.298507, QtGui.QColor(83, 97, 142))
        gradient.setColorAt(1.0, QtGui.QColor(97, 69, 128))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.search_box.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.search_box.setFont(font)
        self.search_box.setObjectName("search_box")
        self.txtSearch = QtWidgets.QLineEdit(self.search_box)
        self.txtSearch.setGeometry(QtCore.QRect(130, 35, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txtSearch.setFont(font)
        self.txtSearch.setStyleSheet("background-color: rgb(248, 248, 248);")
        self.txtSearch.setObjectName("txtSearch")
        self.cmbSearch = QtWidgets.QComboBox(self.search_box)
        self.cmbSearch.setGeometry(QtCore.QRect(20, 35, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cmbSearch.setFont(font)
        self.cmbSearch.setStyleSheet("background-color: rgb(248, 248, 248);")
        self.cmbSearch.setObjectName("cmbSearch")
        self.cmbSearch.addItem("")
        self.cmbSearch.setItemText(0, "")
        self.cmbSearch.addItem("")
        self.cmbSearch.addItem("")
        self.cmbSearch.addItem("")
        self.cmbSearch.addItem("")
        self.cmbSearch.addItem("")
        self.cmbSearch.addItem("")
        self.btnBuscar = QtWidgets.QPushButton(self.search_box)
        self.btnBuscar.setGeometry(QtCore.QRect(492, 35, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnBuscar.setFont(font)
        self.btnBuscar.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.btnBuscar.setObjectName("btnBuscar")

        # -----------  ware_table configuration  -----------
        
        self.ware_table = QtWidgets.QTableWidget(Dialog)
        self.ware_table.setGeometry(QtCore.QRect(0, 130, 1024, 450))
        self.ware_table.setObjectName("ware_table")
        self.ware_table.setColumnCount(8)
        self.ware_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ware_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ware_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ware_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ware_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ware_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ware_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.ware_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.ware_table.setHorizontalHeaderItem(7, item)
        self.ware_table.setColumnWidth(0,80)
        self.ware_table.setColumnWidth(1,120)
        self.ware_table.setColumnWidth(2,300)
        self.ware_table.setColumnWidth(3,120)
        self.ware_table.setColumnWidth(4,80)
        self.ware_table.setColumnWidth(5,200)
        self.ware_table.setColumnWidth(6,40)
        self.ware_table.setColumnWidth(7,54)
        self.ware_table.horizontalHeader().setEnabled(False)
        self.ware_table.setSelectionBehavior(1)
        self.ware_table.setSelectionMode(1)
        self.ware_table.setStyleSheet("selection-background-color: rgb(0, 120, 255);selection-color: rgb(255, 255, 255);")
        # -----------  frame configuration  -----------
        
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 100, 1024, 30))
        self.frame.setStyleSheet("background-color: rgb(57, 57, 57);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(0, 580, 1024, 188))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.298507 rgba(83, 97, 142, 255), stop:1 rgba(97, 69, 128, 255));")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.boxPV = QtWidgets.QGroupBox(self.frame_2)
        self.boxPV.setGeometry(QtCore.QRect(30, 10, 331, 171))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.298507, QtGui.QColor(83, 97, 142))
        gradient.setColorAt(1.0, QtGui.QColor(97, 69, 128))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.298507, QtGui.QColor(83, 97, 142))
        gradient.setColorAt(1.0, QtGui.QColor(97, 69, 128))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.298507, QtGui.QColor(83, 97, 142))
        gradient.setColorAt(1.0, QtGui.QColor(97, 69, 128))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.298507, QtGui.QColor(83, 97, 142))
        gradient.setColorAt(1.0, QtGui.QColor(97, 69, 128))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.298507, QtGui.QColor(83, 97, 142))
        gradient.setColorAt(1.0, QtGui.QColor(97, 69, 128))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.298507, QtGui.QColor(83, 97, 142))
        gradient.setColorAt(1.0, QtGui.QColor(97, 69, 128))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.298507, QtGui.QColor(83, 97, 142))
        gradient.setColorAt(1.0, QtGui.QColor(97, 69, 128))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.298507, QtGui.QColor(83, 97, 142))
        gradient.setColorAt(1.0, QtGui.QColor(97, 69, 128))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 0.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.298507, QtGui.QColor(83, 97, 142))
        gradient.setColorAt(1.0, QtGui.QColor(97, 69, 128))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.boxPV.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.boxPV.setFont(font)
        self.boxPV.setObjectName("boxPV")
        self.lblPV = QtWidgets.QLabel(self.boxPV)
        self.lblPV.setGeometry(QtCore.QRect(160, 20, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lblPV.setFont(font)
        self.lblPV.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.lblPV.setObjectName("lblPV")
        self.lblImg = QtWidgets.QLabel(self.boxPV)
        self.lblImg.setGeometry(QtCore.QRect(10, 30, 131, 131))
        self.lblImg.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.lblImg.setText("")
        self.lblImg.setPixmap(QtGui.QPixmap("../UI/imgs/books_imgs/GN_3.jpg"))
        self.lblImg.setScaledContents(True)
        self.lblImg.setObjectName("lblImg")
        self.lbltxtPrecio = QtWidgets.QLabel(self.boxPV)
        self.lbltxtPrecio.setGeometry(QtCore.QRect(160, 60, 151, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lbltxtPrecio.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbltxtPrecio.setFont(font)
        self.lbltxtPrecio.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.lbltxtPrecio.setObjectName("lbltxtPrecio")
        
        # -----------  boton vender  -----------
        self.btnVender = QtWidgets.QPushButton(self.boxPV)
        self.btnVender.setGeometry(QtCore.QRect(160, 117, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnVender.setFont(font)
        self.btnVender.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.btnVender.setObjectName("btnVender")
        self.btnVender.clicked.connect(self.printCurrent)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # -----------  load_data  -----------
        self.loadData()

    def printCurrent(self):
        temp = self.ware_table.currentRow()
        self.ware_table.clearSelection()
        self.ware_table.setCurrentCell(temp,0)
        print(temp)




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Genesis - [Museo del libro]"))
        self.search_box.setTitle(_translate("Dialog", "Cuadro de busqueda"))
        self.cmbSearch.setItemText(1, _translate("Dialog", "cod"))
        self.cmbSearch.setItemText(2, _translate("Dialog", "isbn"))
        self.cmbSearch.setItemText(3, _translate("Dialog", "nombre"))
        self.cmbSearch.setItemText(4, _translate("Dialog", "autor"))
        self.cmbSearch.setItemText(5, _translate("Dialog", "editorial"))
        self.btnBuscar.setText(_translate("Dialog", "Buscar"))
        item = self.ware_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "cod"))
        item = self.ware_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "isbn"))
        item = self.ware_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "nombre"))
        item = self.ware_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "autor"))
        item = self.ware_table.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "editorial"))
        item = self.ware_table.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "genero"))
        item = self.ware_table.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "[STC]"))
        item = self.ware_table.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "[STGO]"))


        self.boxPV.setTitle(_translate("Dialog", "Cuadro de venta"))
        self.lblPV.setText(_translate("Dialog", "P.Venta:"))
        self.lbltxtPrecio.setText(_translate("Dialog", "S/.50"))
        self.btnVender.setText(_translate("Dialog", "Vender"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
