import sys 
from PyQt5 import QtWidgets, uic

class Ventana (QtWidgets.QMainWindow):
    def __init__(self, padre=None): 
        QtWidgets.QMainWindow.__init__(self,padre)
        uic.loadUi ("Practica 4.ui", self)

        self.PushButton.clicked.connect(self.funcion)

        self.radioButton.toggled.connect(self.RadioSel)
        self.radioButton_2.toggled.connect(self.RadioSel)

    def RadioSel (self):
        self.radio= self.sender()

    def funcion (self):
        v1 = self.checkBox.isChecked ()
        v2 = self.checkBox_2.isChecked ()
        if v1 == True and v2 == True:
            print("CheckBox 1 y 2 activados")
        elif v1 == True and v2 == False:
            print("CheckBox 1 activado y CheckBox 2 desactivado")
        elif v1 == False and v2 == True:
            print("CheckBox 1 desactivado y CheckBox 2 activado")
        else:
            print("CheckBox 1 y 2 desactivados")
        try:
            print(self.radio.text()+" activado ")
        except:
            print("RadioButtons desactivados")

app = QtWidgets.QApplication(sys.argv)
miVentana = Ventana ()
miVentana.show()
sys.exit(app.exec_())
