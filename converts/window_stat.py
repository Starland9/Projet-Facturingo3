# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_stat.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(748, 600)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(9999999, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.tableVente = QtWidgets.QTableWidget(self.centralwidget)
        self.tableVente.setRowCount(10)
        self.tableVente.setObjectName("tableVente")
        self.tableVente.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableVente.setHorizontalHeaderItem(0, item)
        self.tableVente.horizontalHeader().setVisible(False)
        self.tableVente.horizontalHeader().setStretchLastSection(True)
        self.tableVente.verticalHeader().setVisible(False)
        self.tableVente.verticalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableVente, 3, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        self.btn_actu = QtWidgets.QPushButton(self.centralwidget)
        self.btn_actu.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_actu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_actu.setObjectName("btn_actu")
        self.gridLayout.addWidget(self.btn_actu, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.tableClt = QtWidgets.QTableWidget(self.centralwidget)
        self.tableClt.setRowCount(10)
        self.tableClt.setObjectName("tableClt")
        self.tableClt.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableClt.setHorizontalHeaderItem(0, item)
        self.tableClt.horizontalHeader().setVisible(False)
        self.tableClt.horizontalHeader().setStretchLastSection(True)
        self.tableClt.verticalHeader().setVisible(False)
        self.tableClt.verticalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableClt, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 300))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("ui/../images/stat.png"))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Les meilleurs clients\n"
""))
        self.label.setText(_translate("MainWindow", "Statistiques"))
        self.label_3.setText(_translate("MainWindow", "Les articles les plus vendus"))
        self.btn_actu.setText(_translate("MainWindow", "OK"))
        self.label_4.setText(_translate("MainWindow", "\n"
"\n"
"Niveau du marché de l\'entreprise\n"
"\n"
""))
