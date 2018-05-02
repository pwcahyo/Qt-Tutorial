# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(441, 339)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 421, 321))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEditNama = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditNama.setObjectName("lineEditNama")
        self.verticalLayout.addWidget(self.lineEditNama)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButtonTambah = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonTambah.setObjectName("pushButtonTambah")
        self.verticalLayout.addWidget(self.pushButtonTambah)
        self.pushButtonHapusSemua = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonHapusSemua.setObjectName("pushButtonHapusSemua")
        self.verticalLayout.addWidget(self.pushButtonHapusSemua)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.listWidgetNama = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidgetNama.setObjectName("listWidgetNama")
        self.horizontalLayout.addWidget(self.listWidgetNama)

        self.retranslateUi(Form)
        self.pushButtonHapusSemua.clicked.connect(self.listWidgetNama.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Masukan Nama"))
        self.pushButtonTambah.setText(_translate("Form", "Tambahkan"))
        self.pushButtonHapusSemua.setText(_translate("Form", "Hapus Semua"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

