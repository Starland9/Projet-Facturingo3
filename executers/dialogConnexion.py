import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

from converts import dialog_connexion

connexion = sqlite3.connect("Database/database.db")
c = connexion.cursor()


class Connexion(QDialog, dialog_connexion.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.goodLogin = None
        self.goodPassword = None
        self.setupUi(self)
        self.ok = False
        self.connectActions()
        self.setLoginInfos()

    def connectActions(self):
        self.btn_submit.clicked.connect(self.submit)
        self.btn_reset.clicked.connect(self.reset)
        self.showPass.stateChanged.connect(self.setPassViewMode)
        self.souvenir.stateChanged.connect(self.souvenirMe)

    def setLoginInfos(self):
        infos = c.execute("SELECT login, mdp FROM ADMIN").fetchone()
        self.goodLogin = infos[0]
        self.goodPassword = infos[1]

    def submit(self):
        if self.verify():
            self.ok = True
            self.close()

    def reset(self):
        self.close()

    def setPassViewMode(self):
        if self.showPass.checkState() == 0:
            self.mpdLineEdit.setEchoMode(self.mpdLineEdit.Password)
        else:
            self.mpdLineEdit.setEchoMode(self.mpdLineEdit.Normal)

    def souvenirMe(self):
        pass

    def verify(self):
        if self.mpdLineEdit.text() == self.goodPassword and self.loginLineEdit.text() == self.goodLogin:
            return True
        else:
            QMessageBox.information(self, "Vérification", "Veuillez entrer des informations correctes")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    connexion = Connexion()
    connexion.show()
    app.exec_()
