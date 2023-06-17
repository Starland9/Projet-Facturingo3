import sqlite3
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from converts import window_stat

connexion = sqlite3.connect("Database/database.db")
c = connexion.cursor()


class Stat(QMainWindow, window_stat.Ui_MainWindow):
    def __init__(self):
        super(Stat, self).__init__(parent=None)
        self.setupUi(self)
        # self.showFullScreen()
        self.showMaximized()
        self.fillClts()
        self.fillVnt()

        self.connectActions()

    def connectActions(self):
        self.btn_actu.clicked.connect(self.close)

    def fillClts(self):
        clts = c.execute("SELECT nom FROM CLIENTS ORDER BY nom DESC").fetchmany(10)
        for i in range(len(clts)):
            self.tableClt.setItem(i, 0, QTableWidgetItem(clts[i][0]))

    def fillVnt(self):
        desis = c.execute("SELECT desi FROM STOCKS ORDER BY desi DESC").fetchmany(10)
        for i in range(len(desis)):
            self.tableVente.setItem(i, 0, QTableWidgetItem(desis[i][0]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stat = Stat()
    stat.show()
    app.exec_()
