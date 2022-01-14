import sqlite3
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox

from converts import window_client
from executers import dialogModifClt, dialogDelClt

connexion = sqlite3.connect("Database/database.db")
c = connexion.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS CLIENTS(
            id TEXT PRIMARY KEY UNIQUE,
            nom TEXT,
            tel TEXT,
            date TEXT,
            email TEXT
            )""")


def delClient(identifiant):
    identifiant = (identifiant,)
    c.execute(f"DELETE FROM CLIENTS WHERE id = ?", identifiant)
    # connexion.commit()


class Client(QMainWindow, window_client.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.remove_clt = None
        self.modif_clt = None
        self.setupUi(self)

        self.showMaximized()
        self.connectActions()
        self.fillTable()

    def modifClient(self, nom, newId, newTel, newDate, newMail):
        donnee = (newId, newTel, newDate, newMail, nom)
        try:
            c.execute(f"UPDATE CLIENTS SET (id, tel, date, email) = (?, ?, ?, ?) "
                      f"WHERE nom = ?", donnee)
        except sqlite3.IntegrityError:
            QMessageBox.information(self, "Information", f"L'identifiant que vous attribuez à {nom} est déja "
                                                         f"utilisé.\nVeuillez en attribuer un autre.")

    def connectActions(self):
        self.btn_modif_clt.clicked.connect(self.modifClt)
        self.btn_remove_clt.clicked.connect(self.removeClt)
        self.line_search.textEdited.connect(self.search)

    def search(self):
        self.table_clt.setRowCount(0)
        items = []
        text = self.line_search.text()
        stock = c.execute(" SELECT * FROM CLIENTS ORDER BY nom").fetchall()
        for i in range(len(stock)):
            desi = stock[i][1]
            if desi.__contains__(text.capitalize()) or desi.__contains__(text.casefold()) or desi.__contains__(
                    text.swapcase()):
                items.append(stock[i])
        for i in range(len(items)):
            self.table_clt.setRowCount(self.table_clt.rowCount() + 1)
            for j in range(len(items[i])):
                self.table_clt.setItem(i, j, QTableWidgetItem(str(items[i][j])))

    def modifClt(self):
        self.modif_clt = dialogModifClt.ModifClt()
        self.modif_clt.exec_()
        if self.modif_clt.ok:
            identifiant, nom, tel, date, mail = self.modif_clt.getInfos()
            self.modifClient(nom, identifiant, tel, date, mail)
            self.fillTable()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        connexion.commit()

    def removeClt(self):
        self.remove_clt = dialogDelClt.DelClt()
        self.remove_clt.exec_()
        if self.remove_clt.ok:
            identifiant, clt = self.remove_clt.getInfos()
            delClient(identifiant)
            self.fillTable()

    def fillTable(self):
        clients = c.execute("SELECT * FROM CLIENTS ORDER BY nom").fetchall()
        self.table_clt.setRowCount(len(clients))
        for i in range(len(clients)):
            for j in range(5):
                self.table_clt.setItem(i, j, QTableWidgetItem(str(clients[i][j])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = Client()
    client.show()
    app.exec_()
