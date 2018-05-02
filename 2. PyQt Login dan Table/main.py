import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from layout.main_layout import Ui_Biodata as main_layout
from layout.login_layout import Ui_Login as login_layout

class ProgramBiodata(login_layout):
	"""Program Biodata"""

	def login(self):
		"""fungsi login"""
		username = self.lineEditUsername.text()
		password = self.lineEditPassword.text()
		if(username == "cahyo" and password == "1234"):
			self.mainWindow = QtWidgets.QDialog()
			self.mainUI = main_layout()
			self.mainUI.setupUi(self.mainWindow)
			loginWindow.hide()
			self.mainUI.labelWarning.hide()
			self.mainWindow.show()

			self.mainUI.pushButtonTambahkan.clicked.connect(self.tambahBiodata)
			self.mainUI.pushButtonHapus.clicked.connect(self.hapusBiodata)
		else:
			self.labelWarning.setText("Username atau Password salah !")
			self.labelWarning.show()

	def __init__(self, dialog):
		login_layout.__init__(self)
		self.setupUi(dialog)
		self.labelWarning.hide()
		self.pushButtonLogin.clicked.connect(self.login)

	def tambahBiodata(self):
		"""fungsi menambah biodata"""
		nama = self.mainUI.lineEditNama.text()
		NIM = self.mainUI.lineEditNIM.text()
		prodi = self.mainUI.lineEditProdi.text()
		hobi = self.mainUI.lineEditHobi.text()
		
		rowPosition = self.mainUI.tableWidgetBiodata.rowCount()
		self.mainUI.tableWidgetBiodata.insertRow(rowPosition)
		self.mainUI.tableWidgetBiodata.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(nama))
		self.mainUI.tableWidgetBiodata.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(NIM))
		self.mainUI.tableWidgetBiodata.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(prodi))
		self.mainUI.tableWidgetBiodata.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(hobi))
		self.mainUI.labelWarning.setText("Data {} berhasil ditambahkan".format(nama))
		self.mainUI.labelWarning.show()

	def hapusBiodata(self):
		"""fungsi menghapus biodata"""
		selectedRow = self.mainUI.tableWidgetBiodata.currentRow()
		nama = self.mainUI.tableWidgetBiodata.item(selectedRow,0).text()
		self.mainUI.tableWidgetBiodata.removeRow(selectedRow)
		self.mainUI.labelWarning.setText("Data {} berhasil dihapus".format(nama))
		self.mainUI.labelWarning.show()


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	loginWindow = QtWidgets.QDialog()

	loginUI = ProgramBiodata(loginWindow)

	loginWindow.show()
	sys.exit(app.exec_())