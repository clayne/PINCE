# Form implementation generated from reading ui file 'AddAddressManuallyDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(262, 486)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.comboBox_ValueType = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_ValueType.setObjectName("comboBox_ValueType")
        self.horizontalLayout_3.addWidget(self.comboBox_ValueType)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.comboBox_Endianness = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_Endianness.setObjectName("comboBox_Endianness")
        self.horizontalLayout_6.addWidget(self.comboBox_Endianness)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.widget_Repr = QtWidgets.QWidget(parent=Dialog)
        self.widget_Repr.setObjectName("widget_Repr")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_Repr)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_Hex = QtWidgets.QCheckBox(parent=self.widget_Repr)
        self.checkBox_Hex.setObjectName("checkBox_Hex")
        self.horizontalLayout_2.addWidget(self.checkBox_Hex)
        self.checkBox_Signed = QtWidgets.QCheckBox(parent=self.widget_Repr)
        self.checkBox_Signed.setObjectName("checkBox_Signed")
        self.horizontalLayout_2.addWidget(self.checkBox_Signed)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.widget_Repr)
        self.widget_Length = QtWidgets.QWidget(parent=Dialog)
        self.widget_Length.setObjectName("widget_Length")
        self.horizontalLayout_Length = QtWidgets.QHBoxLayout(self.widget_Length)
        self.horizontalLayout_Length.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Length.setObjectName("horizontalLayout_Length")
        self.label_Length = QtWidgets.QLabel(parent=self.widget_Length)
        self.label_Length.setObjectName("label_Length")
        self.horizontalLayout_Length.addWidget(self.label_Length)
        self.lineEdit_Length = QtWidgets.QLineEdit(parent=self.widget_Length)
        self.lineEdit_Length.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_Length.setInputMask("")
        self.lineEdit_Length.setText("10")
        self.lineEdit_Length.setObjectName("lineEdit_Length")
        self.horizontalLayout_Length.addWidget(self.lineEdit_Length)
        self.checkBox_ZeroTerminate = QtWidgets.QCheckBox(parent=self.widget_Length)
        self.checkBox_ZeroTerminate.setChecked(True)
        self.checkBox_ZeroTerminate.setObjectName("checkBox_ZeroTerminate")
        self.horizontalLayout_Length.addWidget(self.checkBox_ZeroTerminate)
        spacerItem3 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_Length.addItem(spacerItem3)
        self.verticalLayout_3.addWidget(self.widget_Length)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.widget_Pointer = QtWidgets.QWidget(parent=Dialog)
        self.widget_Pointer.setEnabled(True)
        self.widget_Pointer.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_Pointer.setObjectName("widget_Pointer")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_Pointer)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_Pointers = QtWidgets.QVBoxLayout()
        self.verticalLayout_Pointers.setObjectName("verticalLayout_Pointers")
        self.label_BaseAddress = QtWidgets.QLabel(parent=self.widget_Pointer)
        self.label_BaseAddress.setObjectName("label_BaseAddress")
        self.verticalLayout_Pointers.addWidget(self.label_BaseAddress)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_PtrStartAddress = QtWidgets.QLineEdit(parent=self.widget_Pointer)
        self.lineEdit_PtrStartAddress.setObjectName("lineEdit_PtrStartAddress")
        self.horizontalLayout_4.addWidget(self.lineEdit_PtrStartAddress)
        self.label_BaseAddressDeref = QtWidgets.QLabel(parent=self.widget_Pointer)
        self.label_BaseAddressDeref.setText("-> <font color=red>??</font>")
        self.label_BaseAddressDeref.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_BaseAddressDeref.setObjectName("label_BaseAddressDeref")
        self.horizontalLayout_4.addWidget(self.label_BaseAddressDeref)
        self.verticalLayout_Pointers.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_AddOffset = QtWidgets.QPushButton(parent=self.widget_Pointer)
        self.pushButton_AddOffset.setObjectName("pushButton_AddOffset")
        self.horizontalLayout_5.addWidget(self.pushButton_AddOffset)
        self.pushButton_RemoveOffset = QtWidgets.QPushButton(parent=self.widget_Pointer)
        self.pushButton_RemoveOffset.setObjectName("pushButton_RemoveOffset")
        self.horizontalLayout_5.addWidget(self.pushButton_RemoveOffset)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_Pointers.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addLayout(self.verticalLayout_Pointers)
        self.gridLayout.addWidget(self.widget_Pointer, 7, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_Description = QtWidgets.QLineEdit(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Description.sizePolicy().hasHeightForWidth())
        self.lineEdit_Description.setSizePolicy(sizePolicy)
        self.lineEdit_Description.setText("")
        self.lineEdit_Description.setObjectName("lineEdit_Description")
        self.verticalLayout.addWidget(self.lineEdit_Description)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMaximumSize(QtCore.QSize(16777215, 35))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 9, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem5, 8, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_Address = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_Address.setText("")
        self.lineEdit_Address.setObjectName("lineEdit_Address")
        self.horizontalLayout.addWidget(self.lineEdit_Address)
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setText("=")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_Value = QtWidgets.QLabel(parent=Dialog)
        self.label_Value.setText("")
        self.label_Value.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_Value.setObjectName("label_Value")
        self.horizontalLayout.addWidget(self.label_Value)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.checkBox_IsPointer = QtWidgets.QCheckBox(parent=Dialog)
        self.checkBox_IsPointer.setObjectName("checkBox_IsPointer")
        self.gridLayout.addWidget(self.checkBox_IsPointer, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Address Manually"))
        self.label_5.setText(_translate("Dialog", "Type:"))
        self.label_3.setText(_translate("Dialog", "Endianness:"))
        self.checkBox_Hex.setText(_translate("Dialog", "Hex"))
        self.checkBox_Signed.setText(_translate("Dialog", "Signed"))
        self.label_Length.setText(_translate("Dialog", "Length:"))
        self.checkBox_ZeroTerminate.setText(_translate("Dialog", "Zero-Terminated"))
        self.label_BaseAddress.setText(_translate("Dialog", "Base Address:"))
        self.pushButton_AddOffset.setText(_translate("Dialog", "Add Offset"))
        self.pushButton_RemoveOffset.setText(_translate("Dialog", "Remove Offset"))
        self.label_4.setText(_translate("Dialog", "Description:"))
        self.label.setText(_translate("Dialog", "Address:"))
        self.checkBox_IsPointer.setText(_translate("Dialog", "Pointer"))
