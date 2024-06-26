# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_modif_clt.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 420)
        Dialog.setMinimumSize(QtCore.QSize(650, 420))
        Dialog.setMaximumSize(QtCore.QSize(650, 420))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 20, 284, 18))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 60, 581, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setContentsMargins(20, 20, 20, 0)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.dSignationLabel = QtWidgets.QLabel(self.layoutWidget)
        self.dSignationLabel.setObjectName("dSignationLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.dSignationLabel)
        self.idLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idLineEdit.sizePolicy().hasHeightForWidth())
        self.idLineEdit.setSizePolicy(sizePolicy)
        self.idLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.idLineEdit.setSizeIncrement(QtCore.QSize(0, 0))
        self.idLineEdit.setObjectName("idLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.idLineEdit)
        self.nomEtPrNomLabel = QtWidgets.QLabel(self.layoutWidget)
        self.nomEtPrNomLabel.setObjectName("nomEtPrNomLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nomEtPrNomLabel)
        self.nDeTLPhoneLabel = QtWidgets.QLabel(self.layoutWidget)
        self.nDeTLPhoneLabel.setObjectName("nDeTLPhoneLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.nDeTLPhoneLabel)
        self.spin_telphone = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_telphone.sizePolicy().hasHeightForWidth())
        self.spin_telphone.setSizePolicy(sizePolicy)
        self.spin_telphone.setMinimumSize(QtCore.QSize(0, 40))
        self.spin_telphone.setSizeIncrement(QtCore.QSize(0, 0))
        self.spin_telphone.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spin_telphone.setProperty("showGroupSeparator", True)
        self.spin_telphone.setMaximum(999999999)
        self.spin_telphone.setProperty("value", 6)
        self.spin_telphone.setObjectName("spin_telphone")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spin_telphone)
        self.dateDeNaissanceLabel = QtWidgets.QLabel(self.layoutWidget)
        self.dateDeNaissanceLabel.setObjectName("dateDeNaissanceLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.dateDeNaissanceLabel)
        self.dateDeNaissanceDateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateDeNaissanceDateEdit.sizePolicy().hasHeightForWidth())
        self.dateDeNaissanceDateEdit.setSizePolicy(sizePolicy)
        self.dateDeNaissanceDateEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.dateDeNaissanceDateEdit.setSizeIncrement(QtCore.QSize(0, 0))
        self.dateDeNaissanceDateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateDeNaissanceDateEdit.setCalendarPopup(True)
        self.dateDeNaissanceDateEdit.setObjectName("dateDeNaissanceDateEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dateDeNaissanceDateEdit)
        self.adresseMailLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adresseMailLineEdit.sizePolicy().hasHeightForWidth())
        self.adresseMailLineEdit.setSizePolicy(sizePolicy)
        self.adresseMailLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.adresseMailLineEdit.setSizeIncrement(QtCore.QSize(0, 0))
        self.adresseMailLineEdit.setObjectName("adresseMailLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.adresseMailLineEdit)
        self.adresseMailLabel = QtWidgets.QLabel(self.layoutWidget)
        self.adresseMailLabel.setObjectName("adresseMailLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.adresseMailLabel)
        self.comboChoixCllt = QtWidgets.QComboBox(self.layoutWidget)
        self.comboChoixCllt.setMinimumSize(QtCore.QSize(0, 40))
        self.comboChoixCllt.setObjectName("comboChoixCllt")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboChoixCllt)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(220, 350, 371, 52))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_submit = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_submit.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_submit.setObjectName("btn_submit")
        self.horizontalLayout.addWidget(self.btn_submit)
        self.btn_reset = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_reset.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_reset.setObjectName("btn_reset")
        self.horizontalLayout.addWidget(self.btn_reset)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Modifier un client"))
        self.label.setText(_translate("Dialog", "Modifier les informations sur un client"))
        self.dSignationLabel.setText(_translate("Dialog", "Identifiant : "))
        self.nomEtPrNomLabel.setText(_translate("Dialog", "Nom et prénom : "))
        self.nDeTLPhoneLabel.setText(_translate("Dialog", "N° de téléphone : "))
        self.spin_telphone.setPrefix(_translate("Dialog", "+237"))
        self.dateDeNaissanceLabel.setText(_translate("Dialog", "Date de naissance : "))
        self.adresseMailLabel.setText(_translate("Dialog", "Adresse mail : "))
        self.btn_submit.setText(_translate("Dialog", "Enregistrer"))
        self.btn_reset.setText(_translate("Dialog", "Annuler"))
