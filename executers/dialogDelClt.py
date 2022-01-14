import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QDialog

from converts import dialog_del_clt

connexion = sqlite3.connect("Database/database.db")
c = connexion.cursor()


class DelClt(QDialog, dialog_del_clt.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ok = False
        self.fillNames()
        self.setId()
        self.connectActions()

    def connectActions(self):
        self.btn_reset.clicked.connect(self.annuler)
        self.btn_submit.clicked.connect(self.enregistrer)
        self.combo_nomP.currentIndexChanged.connect(self.setId)

    def enregistrer(self):
        self.ok = True
        self.close()

    def annuler(self):
        self.close()

    def getInfos(self):
        identifiant = self.identifiant_lineEdit.text()
        clt = self.combo_nomP.currentText()
        return identifiant, clt

    def fillNames(self):
        names = []
        with connexion:
            n = c.execute("SELECT nom FROM CLIENTS ORDER BY nom").fetchall()
        for i in n:
            names.append(i[0])
        self.combo_nomP.addItems(names)

    def setId(self):
        nom = self.combo_nomP.currentText()
        nom = (nom, )
        with connexion:
            iden = c.execute("SELECT id FROM CLIENTS WHERE nom = ?", nom).fetchone()
        try:
            self.identifiant_lineEdit.setText(iden[0])
        except TypeError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    delclt = DelClt()
    delclt.show()
    app.exec_()
