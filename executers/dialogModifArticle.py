import sqlite3
import sys

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QDialog

from converts import dialog_modif_article

connexion = sqlite3.connect("Database/database.db")
c = connexion.cursor()


def getArticles():
    articles = []
    with connexion:
        a = c.execute(f"SELECT desi FROM STOCKS ORDER BY desi").fetchall()
    for i in a:
        articles.append(i[0])
    return articles


class Article(QDialog, dialog_modif_article.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ok = False
        self.articles = getArticles()
        self.connectAction()
        self.setCode()

    def connectAction(self):
        self.setCurrentDate()
        self.fillArticle()
        self.btn_modifer.clicked.connect(self.enregistrer)
        self.btn_annuler.clicked.connect(self.annuler)
        self.combochoixArticle.currentIndexChanged.connect(self.setCode)

    def fillArticle(self):
        self.combochoixArticle.addItems(self.articles)

    def setCode(self):
        try:
            a = self.combochoixArticle.currentText()
            art = (a,)
            with connexion:
                code = c.execute(f"SELECT code,prix,qtte FROM STOCKS WHERE desi = ?", art).fetchone()
            self.codeLineEdit.setText(code[0])
            self.spinPrix.setValue(int(code[1]))
            self.qtteSpin.setValue(int(code[2]))
        except TypeError:
            pass

    def setCurrentDate(self):
        self.dateModifW.setDate(QDate.currentDate())

    def enregistrer(self):
        self.ok = True
        self.close()

    def annuler(self):
        self.close()

    def getInfos(self):
        code = self.codeLineEdit.text()
        articleChoix = self.combochoixArticle.currentText()
        prix = self.spinPrix.value().__str__()
        dateModif = self.dateModifW.date().toString("dd/MM/yyyy")
        qtte = self.qtteSpin.value().__str__()
        return code, articleChoix, prix, qtte, dateModif


if __name__ == '__main__':
    app = QApplication(sys.argv)
    article = Article()
    article.show()
    app.exec_()
