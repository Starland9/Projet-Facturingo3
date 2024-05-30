import sys

from PyQt5.QtWidgets import QApplication

from executers import windowHome

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyleSheet(open("styles/futurist.qss", "r").read())
    home = windowHome.Home()
    home.show()
    app.exec_()
