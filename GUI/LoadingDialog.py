# Form implementation generated from reading ui file 'LoadingDialog.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(107, 71)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_Animated = QtWidgets.QLabel(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Animated.sizePolicy().hasHeightForWidth())
        self.label_Animated.setSizePolicy(sizePolicy)
        self.label_Animated.setText("")
        self.label_Animated.setScaledContents(False)
        self.label_Animated.setObjectName("label_Animated")
        self.horizontalLayout.addWidget(self.label_Animated)
        self.label_StatusText = QtWidgets.QLabel(parent=Dialog)
        self.label_StatusText.setObjectName("label_StatusText")
        self.horizontalLayout.addWidget(self.label_StatusText)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.pushButton_Cancel = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.gridLayout.addWidget(self.pushButton_Cancel, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.label_StatusText.setText(_translate("Dialog", "Processing"))
        self.pushButton_Cancel.setText(_translate("Dialog", "Cancel"))