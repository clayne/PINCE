# Form implementation generated from reading ui file 'TrackSelectorDialog.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(165, 99)
        Dialog.setWindowTitle("")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton_Pointer = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Pointer.setObjectName("pushButton_Pointer")
        self.verticalLayout.addWidget(self.pushButton_Pointer)
        self.pushButton_Pointed = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Pointed.setObjectName("pushButton_Pointed")
        self.verticalLayout.addWidget(self.pushButton_Pointed)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", "Select an address to track"))
        self.pushButton_Pointer.setText(_translate("Dialog", "Pointer"))
        self.pushButton_Pointed.setText(_translate("Dialog", "Pointed Address"))