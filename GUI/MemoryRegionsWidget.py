# Form implementation generated from reading ui file 'MemoryRegionsWidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(684, 539)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget_MemoryRegions = QtWidgets.QTableWidget(Form)
        self.tableWidget_MemoryRegions.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_MemoryRegions.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_MemoryRegions.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_MemoryRegions.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableWidget_MemoryRegions.setWordWrap(False)
        self.tableWidget_MemoryRegions.setObjectName("tableWidget_MemoryRegions")
        self.tableWidget_MemoryRegions.setColumnCount(4)
        self.tableWidget_MemoryRegions.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_MemoryRegions.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_MemoryRegions.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_MemoryRegions.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_MemoryRegions.setHorizontalHeaderItem(3, item)
        self.tableWidget_MemoryRegions.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_MemoryRegions.verticalHeader().setVisible(False)
        self.tableWidget_MemoryRegions.verticalHeader().setDefaultSectionSize(16)
        self.tableWidget_MemoryRegions.verticalHeader().setMinimumSectionSize(16)
        self.gridLayout.addWidget(self.tableWidget_MemoryRegions, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Memory Regions"))
        self.tableWidget_MemoryRegions.setSortingEnabled(True)
        item = self.tableWidget_MemoryRegions.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Regions"))
        item = self.tableWidget_MemoryRegions.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Perms"))
        item = self.tableWidget_MemoryRegions.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Offset"))
        item = self.tableWidget_MemoryRegions.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Path"))
