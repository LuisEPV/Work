import sys 
from PyQt5 import QtWidgets, uic

class Ventana (QtWidgets.QMainWindow):
    def __init__(self, padre=None): 
        QtWidgets.QMainWindow.__init__(self,padre)
        uic.loadUi ("practica 6.ui", self)

        self.pushButton.clicked.connect(self.mostrar)
        self.pushButton_2.clicked.connect(self.agregar)

        for i in range (20):
            self.comboBox.insertItem(self.comboBox.count(), "Elemento ()".format(i))


    def agregar (self):
        if self.lineEdit.text() != "" :
            self.comboBox.insertItem(self.comboBox.count (), self.lineEdit.text ())
            self.lineEdit.clear ()
        else:
            pass

    def mostrar (self):
        self.label.setText ("Seleccion "+self.comboBox.currentText())
 

app = QtWidgets.QApplication(sys.argv)
miVentana = Ventana ()
miVentana.show()
sys.exit(app.exec_())