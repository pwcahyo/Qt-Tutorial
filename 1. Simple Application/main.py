import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from layout import Ui_Form

class ProgramNama(Ui_Form):
	def __init__(self, dialog):
		Ui_Form.__init__(self)
		self.setupUi(dialog)
		self.pushButtonTambah.clicked.connect(self.tambahNamakeDalamList)

	def tambahNamakeDalamList(self):
		nama = self.lineEditNama.text()
		self.listWidgetNama.addItem(nama)

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()

	prog = ProgramNama(dialog)

	dialog.show()
	sys.exit(app.exec_())