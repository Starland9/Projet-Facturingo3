import random
import shutil
import sqlite3
import sys
from datetime import date

import openpyxl
from PyQt5 import QtGui
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox

from converts import window_new_achat

connexion = sqlite3.connect("Database/database.db")
c = connexion.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS CLIENTS(
            id TEXT PRIMARY KEY UNIQUE,
            nom TEXT,
            tel TEXT,
            date TEXT,
            email TEXT
            )""")

sample = "Database/sample.xlsx"


def getDes():
    des = []
    infos = c.execute("SELECT desi FROM STOCKS ORDER BY desi").fetchall()
    for i in infos:
        des.append(i[0])
    return des


class NewAchat(QMainWindow, window_new_achat.Ui_MainWindow):
    def __init__(self):
        super(NewAchat, self).__init__(parent=None)
        self.setupUi(self)
        self.showMaximized()
        self.fillComboClients()
        self.designations = getDes()
        self.identifiantLineEdit.setMaxLength(7)
        self.connectActions()

    def connectActions(self):
        self.comboDesin.addItems(self.designations)
        self.nomEtPrNomLineEdit.textChanged.connect(self.setId)
        self.btn_add_achat.clicked.connect(self.addAchat)
        self.btn_save.clicked.connect(self.enregistrer)
        self.btn_open.clicked.connect(self.ouvrir)
        self.btn_export.clicked.connect(self.exportFacture)
        self.combo_choix_clt.currentIndexChanged.connect(self.setAutoInfosClient)
        self.comboDesin.currentIndexChanged.connect(self.setAutoInfosDes)
        self.qtteSpin.valueChanged.connect(self.setPrixTotal)

    def addNewClient(self, identifiant, nom, tel, daten, mail):
        donnee = (identifiant, nom, tel, daten, mail)
        try:
            c.execute(f"INSERT INTO CLIENTS VALUES(?, ?, ?, ?, ?)", donnee)
            connexion.commit()
        except sqlite3.IntegrityError:
            QMessageBox.information(self, f"Information", "Ce client existe déja, plus besoin de l'enregistrer")

    def setPrixTotal(self):
        prixTotal = self.qtteSpin.value() * self.prixSpin.value()
        self.prixTotalSpinBox.setValue(prixTotal)

    def setAutoInfosDes(self):
        des = self.comboDesin.currentText()
        des = (des,)
        d = c.execute("SELECT code, prix FROM STOCKS WHERE desi = ?", des).fetchone()
        self.code_lineEdit.setText(d[0])
        self.prixSpin.setValue(int(d[1]))
        self.setPrixTotal()

    def addAchat(self):
        if self.verify():
            code = self.code_lineEdit.text()
            des = self.comboDesin.currentText()
            qtte = self.qtteSpin.value().__str__()
            prix = self.prixSpin.value().__str__()
            prixTotal = str(int(qtte) * int(prix))
            item_code = QTableWidgetItem(code)
            item_des = QTableWidgetItem(des)
            item_qtte = QTableWidgetItem(qtte)
            item_prix = QTableWidgetItem(prix)
            item_prixTotal = QTableWidgetItem(prixTotal)
            for i in range(self.tableAchat.rowCount()):
                if self.tableAchat.item(i, 0) is None:
                    self.tableAchat.setItem(i, 0, item_code)
                    self.tableAchat.setItem(i, 1, item_des)
                    self.tableAchat.setItem(i, 3, item_qtte)
                    self.tableAchat.setItem(i, 2, item_prix)
                    self.tableAchat.setItem(i, 4, item_prixTotal)
                    break
            self.setPrixTOTAL()
            self.setNbreArticles()
            self.resetInfoAchat()

    def verify(self):
        if not self.code_lineEdit.text() == "":
            return True
        else:
            QMessageBox.information(self, "Vérification", "Veuillez ajouter un article correct à la commande.")

    def verifyClt(self):
        if not self.identifiantLineEdit.text() == "":
            return True
        else:
            QMessageBox.information(self, "Vérification", "Veuillez enregistrer une vraie personne s'il vous plait.")

    def setNbreArticles(self):
        nbre = 0
        for i in range(self.tableAchat.rowCount()):
            if not self.tableAchat.item(i, 0) is None:
                nbre += int(self.tableAchat.item(i, 3).text())
        self.nb_article_spin.setValue(nbre)

    def setPrixTOTAL(self):
        prixT = 0
        for i in range(self.tableAchat.rowCount()):
            if not self.tableAchat.item(i, 0) is None:
                prixT += int(self.tableAchat.item(i, 4).text())
        self.prix_total_spin.setValue(prixT)

    def resetInfoAchat(self):
        self.code_lineEdit.clear()
        self.prixSpin.setValue(0)
        self.qtteSpin.setValue(0)
        self.prixTotalSpinBox.setValue(0)

    def enregistrer(self):
        if self.verifyClt():
            identifiant = self.identifiantLineEdit.text()
            nom = self.nomEtPrNomLineEdit.text()
            tel = self.tel_spin.value().__str__()
            dateNaiss = self.dateDeNaissanceDateEdit.date().toString("dd/MM/yyyy")
            mail = self.adresseEmailLineEdit.text()
            self.addNewClient(identifiant, nom, tel, dateNaiss, mail)

    def ouvrir(self):
        self.tableAchat.clearContents()

    # def exporter(self):
    #     ide = self.identifiantLineEdit.text()
    #     nom = self.nomEtPrNomLineEdit.text()
    #     tel = self.tel_spin.value().__str__()
    #     mail = self.adresseEmailLineEdit.text()

    def exportFacture(self):
        if self.updateQtte():
            # self.enregistrer()

            filename = self.nomEtPrNomLineEdit.text() + "_" + str(date.today())
            myFile = f"Factures/{filename}.xlsx"
            shutil.copyfile(sample, myFile)

            self.insertExcel(myFile)
            client = self.nomEtPrNomLineEdit.text()
            dt = str(date.today())
            d = (client, dt)
            c.execute("INSERT INTO FACTURE (client, date) VALUES (?, ?)", d)
            connexion.commit()
            rep = QMessageBox.information(self, "Succes", f"La facture de {self.nomEtPrNomLineEdit.text()} a été"
                                                          f" crée avec succes !", QMessageBox.Open, QMessageBox.Ok)
            if rep == QMessageBox.Open:
                pass

    def insertExcel(self, filename):
        # On créer un "classeur"
        classeur = openpyxl.load_workbook(filename)
        # On ajoute une feuille au classeur
        feuille = classeur.active

        feuille["F3"] = self.identifiantLineEdit.text()
        feuille["F4"] = self.nomEtPrNomLineEdit.text()
        feuille["F5"] = self.tel_spin.value().__str__()
        feuille["F6"] = self.adresseEmailLineEdit.text()

        n = int(c.execute("SELECT numero FROM FACTURE").fetchall()[-1][0]) + 1
        feuille["F10"] = str(n)
        # feuille["E25"] = self.modeDePayementComboBox.currentText()

        for i in range(0, self.tableAchat.rowCount()):
            if not self.tableAchat.item(i, 0) is None:
                try:
                    feuille[f"B{15 + i}"] = self.tableAchat.item(i, 0).text()
                    feuille[f"C{15 + i}"] = self.tableAchat.item(i, 1).text()
                    feuille[f"D{15 + i}"] = int(self.tableAchat.item(i, 2).text())
                    feuille[f"E{15 + i}"] = int(self.tableAchat.item(i, 3).text())
                    feuille[f"F{15 + i}"] = int(self.tableAchat.item(i, 4).text())
                except AttributeError:
                    break

        classeur.save(filename)
        classeur.close()

        self.updateQtte()

    def updateQtte(self):
        good = True
        for i in range(self.tableAchat.rowCount()):
            if not self.tableAchat.item(i, 0) is None:
                try:
                    code = self.tableAchat.item(i, 0).text()
                    qtte = int(self.tableAchat.item(i, 3).text())
                    cd = (code,)
                    q = c.execute("SELECT qtte FROM STOCKS WHERE code = ?", cd).fetchone()[0]
                    q = int(q)
                    if q < qtte:
                        QMessageBox.warning(self, "Attention stock insuffisant", "Certaines quantité ne suffisent pas"
                                                                                 "en stock")
                        good = False
                        break
                    newQ = q - qtte
                    d = (newQ, code)
                    c.execute("UPDATE STOCKS SET qtte = ? WHERE code = ?", d)
                    connexion.commit()
                except AttributeError:
                    break
        if good:
            return True
        else:
            return False

    def fillComboClients(self):
        infos = []
        noms = c.execute("SELECT nom FROM CLIENTS ORDER BY nom").fetchall()
        for i in noms:
            infos.append(i[0])
        self.combo_choix_clt.addItems(infos)

    def setAutoInfosClient(self):
        client = self.combo_choix_clt.currentText()
        self.nomEtPrNomLineEdit.setText(client)
        clt = (client,)
        infos = c.execute("SELECT id, tel, date, email FROM CLIENTS WHERE nom = ?", clt).fetchone()
        self.identifiantLineEdit.setText(infos[0])
        self.tel_spin.setValue(int(infos[1]))
        d = infos[2].split("/")
        self.dateDeNaissanceDateEdit.setDate(QDate(int(d[2]), int(d[1]), int(d[0])))
        self.adresseEmailLineEdit.setText(infos[3])

    def setId(self):
        i = f"{random.randint(1000, 9999)}{self.nomEtPrNomLineEdit.text()}"
        self.identifiantLineEdit.setText(i)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        connexion.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    achat = NewAchat()
    achat.show()
    app.exec_()
