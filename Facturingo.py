import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from executers import windowHome


if __name__ == '__main__':
    app = QApplication(sys.argv)
    home = windowHome.Home()
    home.show()
    app.exec_()