import sys 
import math
from PyQt5 import QtWidgets, uic
from matplotlib.backends.backend_qt5agg  import  FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg  import  NavigationToolbar2QT as Toolbar
from matplotlib.pyplot   import figure

class Ventana (QtWidgets.QMainWindow):
    def __init__(self, padre=None): 
        QtWidgets.QMainWindow.__init__(self,padre)
        uic.loadUi ("practica 8.ui", self)

        figura = figure(tight_layout=True)
        self.canvas=FigureCanvas(figura)
        toolbar=Toolbar(self.canvas, self)

        self.verticalLayout.addWidget(toolbar)
        self.verticalLayout.addWidget(self.canvas)

        self.ax=figura.add_subplot(111)

        self.pushButton.clicked.connect(self.make_plot)
        



    def make_plot (self):
        
        if (self.lineEdit_3.text()!=""and self.lineEdit_2.text()!="" and self.lineEdit.text()!=""):
            Vp = float(self.lineEdit_3.text())
            fre = float(self.lineEdit_2.text())
            w = 2*math.pi*fre # rad/s
            fi = float(self.lineEdit.text())

       

            def f1 (t):
               return Vp*math.sin(w*t+fi)
            t = []
            v = []

            ciclos = 5
            puntos = 30
            T = 1/fre
            deltat = T
            ti = 0 
            for i in range (puntos*ciclos+1):
                t.append(ti)
                v.append(f1(ti))
                ti= ti + deltat

            self.ax.cla()
            self.ax.plot(t,v)
            self.canvas.draw()
        else:
            print("error en los datos de entrada.\n")
            


app = QtWidgets.QApplication(sys.argv)
miVentana = Ventana ()
miVentana.make_plot()
miVentana.show()
sys.exit(app.exec_())