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