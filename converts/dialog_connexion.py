# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_connexion.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 330)
        Dialog.setMinimumSize(QtCore.QSize(650, 330))
        Dialog.setMaximumSize(QtCore.QSize(650, 330))
        font = QtGui.QFont()
        font.setPointSize(11)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 20, 284, 18))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 60, 581, 131))
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
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dSignationLabel.setFont(font)
        self.dSignationLabel.setObjectName("dSignationLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.dSignationLabel)
        self.loginLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginLineEdit.sizePolicy().hasHeightForWidth())
        self.loginLineEdit.setSizePolicy(sizePolicy)
        self.loginLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.loginLineEdit.setSizeIncrement(QtCore.QSize(0, 0))
        self.loginLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.loginLineEdit.setClearButtonEnabled(True)
        self.loginLineEdit.setObjectName("loginLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.loginLineEdit)
        self.adresseMailLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.adresseMailLabel.setFont(font)
        self.adresseMailLabel.setObjectName("adresseMailLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.adresseMailLabel)
        self.mpdLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpdLineEdit.sizePolicy().hasHeightForWidth())
        self.mpdLineEdit.setSizePolicy(sizePolicy)
        self.mpdLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.mpdLineEdit.setSizeIncrement(QtCore.QSize(0, 0))
        self.mpdLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mpdLineEdit.setClearButtonEnabled(True)
        self.mpdLineEdit.setObjectName("mpdLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mpdLineEdit)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(170, 260, 421, 52))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_submit = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_submit.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.btn_submit.setFont(font)
        self.btn_submit.setObjectName("btn_submit")
        self.horizontalLayout.addWidget(self.btn_submit)
        self.btn_reset = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_reset.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.btn_reset.setFont(font)
        self.btn_reset.setShortcut("")
        self.btn_reset.setObjectName("btn_reset")
        self.horizontalLayout.addWidget(self.btn_reset)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 200, 541, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.showPass = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.showPass.setObjectName("showPass")
        self.horizontalLayout_2.addWidget(self.showPass)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.souvenir = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.souvenir.setObjectName("souvenir")
        self.horizontalLayout_2.addWidget(self.souvenir)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Connexion"))
        self.label.setText(_translate("Dialog", "Connexion"))
        self.dSignationLabel.setText(_translate("Dialog", "Login : "))
        self.adresseMailLabel.setText(_translate("Dialog", "Mot de passe : "))
        self.btn_submit.setText(_translate("Dialog", "Connexion"))
        self.btn_submit.setShortcut(_translate("Dialog", "Return"))
        self.btn_reset.setText(_translate("Dialog", "Annuler"))
        self.showPass.setText(_translate("Dialog", " Afficher le mot de passe"))
        self.souvenir.setText(_translate("Dialog", " Se souvenir de moi"))
