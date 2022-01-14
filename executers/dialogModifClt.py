import sqlite3
import sys


from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QDialog

from converts import dialog_modif_clt

connexion = sqlite3.connect("Database/database.db")
c = connexion.cursor()


class ModifClt(QDialog, dialog_modif_clt.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ok = False
        self.fillComboClt()
        self.fillInfos()
        self.connectAction()

    def connectAction(self):
        self.btn_submit.clicked.connect(self.enregistrer)
        self.btn_reset.clicked.connect(self.annuler)
        self.comboChoixCllt.currentIndexChanged.connect(self.fillInfos)

    def enregistrer(self):
        self.ok = True
        self.close()

    def annuler(self):
        self.close()

    def getInfos(self):
        identifiant = self.idLineEdit.text()
        nom = self.comboChoixCllt.currentText()
        tel = self.spin_telphone.value().__str__()
        date = self.dateDeNaissanceDateEdit.date().toString("dd/MM/yyyy")
        mail = self.adresseMailLineEdit.text()
        return identifiant, nom, tel, date, mail

    def fillComboClt(self):
        clts = []
        cltt = c.execute("SELECT nom FROM CLIENTS ORDER BY nom").fetchall()
        for i in cltt:
            clts.append(i[0])
        self.comboChoixCllt.addItems(clts)

    def fillInfos(self):
        try:
            nom = self.comboChoixCllt.currentText()
            nom = (nom,)
            i = c.execute("SELECT id, tel, date, email FROM CLIENTS WHERE nom = ?", nom).fetchone()
            self.idLineEdit.setText(i[0])
            self.spin_telphone.setValue(int(i[1]))
            d = i[2].split("/")
            self.dateDeNaissanceDateEdit.setDate(QDate(int(d[2]), int(d[1]), int(d[0])))
            self.adresseMailLineEdit.setText(i[3])
        except TypeError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clt = ModifClt()
    clt.show()
    app.exec_()
