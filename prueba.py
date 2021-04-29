'''

******************************************** eventFilter example *************************************
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        qApp.installEventFilter(self) #keyboard control

    def eventFilter(self, obj, event):
        if (event.type() == QtCore.QEvent.KeyPress and obj is self):
            key = event.key()

            if key == Qt.Key_Down:
                print("Down key")
            elif key == Qt.Key_Up:
                print("Up key")

        return super(MainWindow, self).eventFilter(obj, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

*********************************************** change color of qlistview cmb *************************************

# importing libraries
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
  
  
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("Python ")
  
        # setting geometry
        self.setGeometry(100, 100, 600, 400)
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()
  
    # method for widgets
    def UiComponents(self):
  
        # creating a combo box widget
        self.combo_box = QComboBox(self)
  
        # setting geometry of combo box
        self.combo_box.setGeometry(200, 150, 150, 30)


        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.combo_box.setFont(font)
  
        # making combo box editable
        self.combo_box.setEditable(True)
  
        # geek list
        geek_list = ["Sayian", "Super Sayian", "Super Sayian 2", "Super Sayian B"]
  
        # adding list of items to combo box
        self.combo_box.addItems(geek_list)
  
        # adding background color to the view part of combo box
        self.combo_box.setStyleSheet("QListView"
                                     "{"
                                     "background-color: lightgreen;"
                                     "}")
  
  
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())


************************************* message box ********************************************


************************* modelo basico *********************************
ret = QMessageBox.question(self, 'MessageBox', "Click a button", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)

if ret == QMessageBox.Yes:
    print('Button QMessageBox.Yes clicked.')

******************** tipos de botones *************************
QMessageBox.Ok
QMessageBox.Open
QMessageBox.Save
QMessageBox.Cancel
QMessageBox.Close
QMessageBox.Yes
QMessageBox.No
QMessageBox.Abort
QMessageBox.Retry
QMessageBox.Ignore

**************** Tipos de iconos ***********************
msg.setIcon(QMessageBox.Information)
msg.setIcon(QMessageBox.Question)
msg.setIcon(QMessageBox.Warning)
msg.setIcon(QMessageBox.Critical)


     '''