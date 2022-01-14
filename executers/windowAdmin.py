import sqlite3
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication

from converts import window_admin
from executers import dialogModifAdmin

from executers import windowStat


connexion = sqlite3.connect("Database/database.db")
c = connexion.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS ADMIN(
            nom TEXT,
            prenom TEXT,
            date TEXT,
            login TEXT,
            mdp TEXT,
            tel TEXT
            )""")


def modifAdmin(lastmdp, newNom, newPrenom, newDate, login, newMpd, newTel):
    data = (newNom, newPrenom, newDate, login, newMpd, newTel, lastmdp)
    c.execute(f"UPDATE ADMIN SET (nom, prenom, date, login, mdp, tel) = (?, ?, ?, ?, ?, ?) WHERE mdp = ?", data)


def getLastMdpAdmin(login):
    login = (login,)
    mdp = c.execute(f"SELECT mdp FROM ADMIN WHERE login = ?", login).fetchone()
    return mdp[0]


# def addAdmin(nom, prenom, date, login, mdp, tel):
#     c.execute(f"INSERT INTO ADMIN VALUES ({nom}, {prenom}, {date}, {login}, {mdp}, {tel})")


class Admin(QMainWindow, window_admin.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.stat = None
        self.lastMdp = None
        self.modif_admin = None
        self.setupUi(self)
        self.fillInfos()
        self.showMaximized()
        self.connectActions()

    def connectActions(self):
        self.btn_modif.clicked.connect(self.modifAdmin)
        self.btn_stat.clicked.connect(self.showStat)

    def showStat(self):
        self.stat = windowStat.Stat()
        self.stat.show()

    def modifAdmin(self):
        self.modif_admin = dialogModifAdmin.ModifAdmin()
        self.modif_admin.exec_()
        if self.modif_admin.ok:
            nom, prenom, dateNaiss, login, ancien_mdp, mdp, tel = self.modif_admin.getInfos()
            if self.lastMdp == ancien_mdp:
                dateNaiss = dateNaiss.toString("dd/MM/yyyy")
                modifAdmin(ancien_mdp, nom, prenom, dateNaiss, login, mdp, tel)
                self.fillInfos()

    def fillInfos(self):
        infos = c.execute("SELECT * FROM ADMIN").fetchone()
        self.nomLineEdit.setText(infos[0])
        self.prNomLineEdit.setText(infos[1])
        self.dateDeNaissanceLineEdit.setText(infos[2])
        self.loginLineEdit.setText(infos[3])
        self.motDePasseLineEdit.setEchoMode(self.motDePasseLineEdit.Password)
        self.motDePasseLineEdit.setText(infos[4])
        self.nDeTLPhoneSpinBox.setValue(int(infos[5]))
        self.lastMdp = getLastMdpAdmin(self.loginLineEdit.text())

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        connexion.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin = Admin()
    admin.show()
    app.exec_()
