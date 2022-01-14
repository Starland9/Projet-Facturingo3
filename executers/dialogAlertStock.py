import sys

from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem

from converts import window_alert_stock

import sqlite3

connexion = sqlite3.connect("Database/database.db")
c = connexion.cursor()


class Alert(window_alert_stock.Ui_Dialog, QDialog):
    def __init__(self):
        super(Alert, self).__init__(parent=None)
        self.setupUi(self)
        self.go = False
        self.btn_ok.clicked.connect(self.close)
        self.fillAll()

    def fillAll(self):
        n = c.execute("SELECT code, desi, qtte FROM STOCKS WHERE qtte <= 5").fetchall()
        if n:
            self.go = True
        for i in range(len(n)):
            for j in range(len(n[i])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(n[i][j])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    alert = Alert()
    alert.show()
    app.exec_()
