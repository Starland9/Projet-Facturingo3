import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QDialog

from converts import dialog_del_article

connexion = sqlite3.connect("Database/database.db")
c = connexion.cursor()


def getArticles():
    articles = []
    with connexion:
        a = c.execute(f"SELECT desi FROM STOCKS ORDER BY desi").fetchall()
    for i in a:
        articles.append(i[0])
    return articles


class DelArticle(QDialog, dialog_del_article.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ok = False
        self.articles = getArticles()
        self.connectActions()

    def connectActions(self):
        self.fillCombo()
        self.btn_reset.clicked.connect(self.annuler)
        self.btn_remove.clicked.connect(self.enregistrer)

    def getInfos(self):
        articleDel = self.combo_choisir_article.currentText()
        return articleDel

    def enregistrer(self):
        self.ok = True
        self.close()

    def annuler(self):
        self.close()

    def fillCombo(self):
        self.combo_choisir_article.addItems(self.articles)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    delArticle = DelArticle()
    delArticle.show()
    app.exec_()
