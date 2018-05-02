# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout/login_layout.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(339, 187)
        self.loginFrame = QtWidgets.QFrame(Login)
        self.loginFrame.setGeometry(QtCore.QRect(10, 10, 321, 171))
        self.loginFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.loginFrame.setObjectName("loginFrame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.loginFrame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 251, 145))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelCommandLogin = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelCommandLogin.setFont(font)
        self.labelCommandLogin.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCommandLogin.setObjectName("labelCommandLogin")
        self.verticalLayout.addWidget(self.labelCommandLogin)
        self.labelWarning = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelWarning.setAlignment(QtCore.Qt.AlignCenter)
        self.labelWarning.setIndent(-1)
        self.labelWarning.setObjectName("labelWarning")
        self.verticalLayout.addWidget(self.labelWarning)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEditUsername = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditUsername)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEditPassword = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditPassword)
        self.verticalLayout.addLayout(self.formLayout)
        self.pushButtonLogin = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.verticalLayout.addWidget(self.pushButtonLogin)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.labelCommandLogin.setText(_translate("Login", "Silahkan Login"))
        self.labelWarning.setText(_translate("Login", "warning"))
        self.label.setText(_translate("Login", "username"))
        self.label_2.setText(_translate("Login", "password"))
        self.pushButtonLogin.setText(_translate("Login", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

