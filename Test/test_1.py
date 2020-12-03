import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget

class Table(QTableWidget):
     def sizeHint(self):
       horizontal = self.horizontalHeader()
       vertical = self.verticalHeader()
       frame = self.frameWidth() * 2
       return QSize(horizontal.length() + vertical.width() + frame,
                    vertical.length() + horizontal.height() + frame)

class Main(QMainWindow):
     def __init__(self, parent=None):
       super(Main, self).__init__(parent)
       top = Table(3, 5, self)
       self.setCentralWidget(top)

if __name__ == '__main__':
     app = QApplication(sys.argv)
     main = Main()
     main.show()
     sys.exit(app.exec_())