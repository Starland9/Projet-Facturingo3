import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox

from converts import window_gestion_stock
from executers import dialogAddArticle, dialogDelArticle, dialogModifArticle, dialogAlertStock
import sqlite3

connexion = sqlite3.connect("Database/database.db")
c = connexion.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS STOCKS(
            code TEXT PRIMARY KEY,
            desi TEXT,
            prix TEXT,
            qtte TEXT,
            date TEXT
            )""")


def addArticle(code, designation, prix, quantite, date):
    donnee = (code, designation, prix, quantite, date)
    c.execute(f"INSERT INTO STOCKS (code, desi, prix, qtte, date) "
              f"VALUES (?, ?, ?, ?, ?)", donnee)


def delArticle(designation):
    d = (designation,)
    c.execute(f"DELETE FROM STOCKS WHERE desi = ?", d)


def modifArticle(code, newPrix, newQuantite, newDate):
    donnee = (newPrix, newQuantite, newDate, code)
    c.execute(f"UPDATE STOCKS SET (prix, qtte, date) = (?, ?, ?)"
              f"WHERE code = ?", donnee)


class GestionStock(QMainWindow, window_gestion_stock.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.alert = None
        self.modif_article = None
        self.del_article = None
        self.add_article = None
        self.setupUi(self)
        self.showMaximized()
        self.connectActions()
        self.reload()
        self.showAlert()

    def reload(self):
        stock = c.execute("SELECT * FROM STOCKS ORDER BY desi").fetchall()
        self.tableWidget.setRowCount(len(stock))
        for i in range(len(stock)):
            for j in range(len(stock[i])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(stock[i][j])))

    def connectActions(self):
        self.btn_add_article.clicked.connect(self.addArticle)
        self.btn_del_article.clicked.connect(self.delArticle)
        self.btn_modif_article.clicked.connect(self.modifArticle)
        self.line_search.textEdited.connect(self.search)

    def addArticle(self):
        self.add_article = dialogAddArticle.AddArticle()
        self.add_article.exec_()
        if self.add_article.ok:
            code, designation, prix, qtte, dateAjout = self.add_article.getInfos()
            addArticle(code, designation, prix, qtte, dateAjout)
            self.reload()

    def search(self):
        self.tableWidget.setRowCount(0)
        items = []
        text = self.line_search.text()
        stock = c.execute(" SELECT * FROM STOCKS ORDER BY desi").fetchall()
        for i in range(len(stock)):
            desi = stock[i][1]
            if desi.__contains__(text.capitalize()) or desi.__contains__(text.casefold()) or desi.__contains__(
                    text.swapcase()):
                items.append(stock[i])
        for i in range(len(items)):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j in range(len(items[i])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(items[i][j])))


    def delArticle(self):
        self.del_article = dialogDelArticle.DelArticle()
        self.del_article.exec_()
        if self.del_article.ok:
            article = self.del_article.getInfos()
            delArticle(article)
            self.reload()

    def modifArticle(self):
        self.modif_article = dialogModifArticle.Article()
        self.modif_article.exec_()
        if self.modif_article.ok:
            code, article, prix, qtte, date = self.modif_article.getInfos()
            modifArticle(code, prix, qtte, date)
            self.reload()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        connexion.commit()

    def showAlert(self):
        self.alert = dialogAlertStock.Alert()
        self.alert.fillAll()
        if self.alert.go:
            self.alert.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestion = GestionStock()
    gestion.show()
    app.exec_()
