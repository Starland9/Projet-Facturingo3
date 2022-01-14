import sqlite3
import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog

from converts import window_home

from executers import windowAdmin, windowClient, windowGestionStock, dialogConnexion, windowNewAchat

connexion = sqlite3.connect("Database/database.db")
c = connexion.cursor()


class Home(QMainWindow, window_home.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.achat = None
        self.connect = None
        self.winClient = None
        self.winAdmin = None
        self.winStock = None
        self.setupUi(self)
        self.connectActions()

        if not self.connexionOk():
            quit(0)

    def connexionOk(self):
        self.connect = dialogConnexion.Connexion()
        self.connect.exec_()
        if self.connect.ok:
            self.connect.close()
            return True
        else:
            return False

    def connectActions(self):
        self.btn_stock.clicked.connect(self.showStock)
        self.btn_admin.clicked.connect(self.showAdmin)
        self.btn_nouvel_achat.clicked.connect(self.showNewAchat)
        self.btn_infos_clt.clicked.connect(self.showClient)





    def showNewAchat(self):
        self.achat = windowNewAchat.NewAchat()
        self.achat.show()

    def showStock(self):
        self.winStock = windowGestionStock.GestionStock()
        self.winStock.show()

    def showAdmin(self):
        self.winAdmin = windowAdmin.Admin()
        self.winAdmin.show()

    def showClient(self):
        try:
            self.winClient = windowClient.Client()
            self.winClient.show()
        except sqlite3.ProgrammingError:
            QMessageBox.information(self, "Information", "Vous devez redemarer le logiciel pour voir\n"
                                                         "les nouveaux clients ajoutés.")

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:

        reponse = QMessageBox.information(self, "Confirmation de sortie", "\nVoulez-vous vraiment quitter"
                                                                          "\nFacturingo ?\n",
                                          QMessageBox.Yes, QMessageBox.No)
        if reponse == QMessageBox.Yes:
            connexion.commit()
            connexion.close()
            a0.accept()
        else:
            a0.ignore()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     home = Home()
#     home.show()
#     app.exec_()
