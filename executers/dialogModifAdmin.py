import sqlite3
import sys

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDialog, QApplication

from converts import dialog_modif_admin

connexion = sqlite3.connect("Database/database.db")
c = connexion.cursor()


class ModifAdmin(QDialog, dialog_modif_admin.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ok = False
        self.fillInfos()
        self.connectAction()

    def connectAction(self):
        self.btn_submit.clicked.connect(self.enregistrer)
        self.btn_reset.clicked.connect(self.annuler)

    def getInfos(self):
        nom = self.nomLineEdit.text()
        prenom = self.prNomLineEdit.text()
        dateNaiss = self.dateEdit.date()
        login = self.loginLineEdit.text()
        ancien_mdp = self.ancienMotDePasseLineEdit.text()
        mdp = self.motDePasseLineEdit.text()
        tel = self.nDeTLPhoneSpinBox.value()
        return nom, prenom, dateNaiss, login, ancien_mdp, mdp, tel

    def fillInfos(self):
        infos = c.execute("SELECT * FROM ADMIN").fetchone()
        self.nomLineEdit.setText(infos[0])
        self.prNomLineEdit.setText(infos[1])
        d = infos[2].split("/")
        self.dateEdit.setDate(QDate(int(d[2]), int(d[1]), int(d[0])))
        self.loginLineEdit.setText(infos[3])
        self.nDeTLPhoneSpinBox.setValue(int(infos[5]))

    def enregistrer(self):
        self.ok = True
        self.close()

    def annuler(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    modifAdmin = ModifAdmin()
    modifAdmin.show()
    app.exec_()
