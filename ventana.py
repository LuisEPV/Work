import sys 
from PyQt5 import QtWidgets, uic

class ventana (QtWidgets.QMainWindow):
    def __init__ (self, padre=None):
        QtWidgets.QMainWindow.__init__(self,padre)
        uic.loadUi("Ejemplo.ui",self)

        self.setWindowTitle("Ejemplo")

        self.pushButton.clicked.connect(self.funcion)
    
    def funcion (self):
        if self.label.text () =="":
            self.label.text("Hola clase")
        
        else:
            self.label.setText("")

app=QtWidgets.QApplication(sys.argv)
miVentana=ventana()
miVentana.show()
sys.exit(app.exec_())