import sys

from PyQt5.QtWidgets import QDialog, QApplication

from converts import dialog_add_article

class AddArticle(dialog_add_article.Ui_Dialog, QDialog):
    def __init__(self):
        super(AddArticle, self).__init__(parent=None)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    add = AddArticle()
    add.show()
    app.exec_()