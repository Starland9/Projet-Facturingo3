# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_del_article.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 220)
        Dialog.setMinimumSize(QtCore.QSize(650, 220))
        Dialog.setMaximumSize(QtCore.QSize(650, 220))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 10, 154, 18))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 50, 611, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setContentsMargins(20, 20, 20, 0)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.nomEtPrNomLabel = QtWidgets.QLabel(self.layoutWidget)
        self.nomEtPrNomLabel.setObjectName("nomEtPrNomLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nomEtPrNomLabel)
        self.combo_choisir_article = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_choisir_article.setMinimumSize(QtCore.QSize(0, 40))
        self.combo_choisir_article.setObjectName("combo_choisir_article")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.combo_choisir_article)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(150, 150, 470, 52))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_remove = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_remove.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_remove.setObjectName("btn_remove")
        self.horizontalLayout.addWidget(self.btn_remove)
        self.btn_reset = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_reset.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_reset.setObjectName("btn_reset")
        self.horizontalLayout.addWidget(self.btn_reset)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Supprimer un article"))
        self.label.setText(_translate("Dialog", "Supprimer un article"))
        self.nomEtPrNomLabel.setText(_translate("Dialog", "Choisir l\'article à Supprimer : "))
        self.btn_remove.setText(_translate("Dialog", "Supprimer"))
        self.btn_reset.setText(_translate("Dialog", "Annuler"))
