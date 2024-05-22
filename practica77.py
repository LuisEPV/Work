# -*- coding: utf-8 -*-
"""
Ejemplo de ventana básico con FileDialog, QPushButton, QListWidget,
QTabWidget y QLabel
"""
# Importa las librerías necesarias
import sys
from PyQt5 import QtWidgets, uic
import os

# Define la clase de la ventana
class Ventana(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    # Inicializa la ventana y conecta los botones
    def __init__(self, padre=None):
        # Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self, padre)
        # Carga la interfaz gráfica desde el archivo "ejemplo3.ui"
        uic.loadUi("practica 7.ui", self)
        self.cwd = os.getcwd()  # directorio de trabajo

        # Conecta los botones a las funciones correspondientes
        self.pushButton_2.clicked.connect(self.archivo)
        self.pushButton.clicked.connect(self.carpeta)
        self.listWidget.itemClicked.connect(self.mostrar_archivo)

    # Función para manejar la selección de una carpeta
    def carpeta(self):
        """
        Abre una ventana para seleccionar una carpeta y muestra los archivos en el QListWidget
        """
        # Crea el diálogo para seleccionar una carpeta
        carpeta = QtWidgets.QFileDialog.getExistingDirectory(None, 'Seleccionar Carpeta', self.cwd, QtWidgets.QFileDialog.ShowDirsOnly)
        # Borra los nombres de archivos que se están mostrando en la lista
        self.listWidget.clear()

        # Verifica si se seleccionó una carpeta
        if len(carpeta) > 1:
            # Lista de los archivos en la carpeta seleccionada
            listArchivos = os.listdir(carpeta)
            for i in listArchivos:
                self.listWidget.addItem(i)

    # Función para manejar la selección de un archivo
    def archivo(self):
        """
        Abre una ventana para seleccionar un archivo y lo muestra en el QLabel
        """
        archivo = QtWidgets.QFileDialog.getOpenFileName(self, "Abrir archivo", self.cwd)
        self.label_2.setText("Archivo seleccionado: " + archivo[0])

    # Función para mostrar la ruta del archivo seleccionado
    def mostrar_archivo(self, item):
        """
        Obtiene y muestra la ruta del archivo seleccionado de la lista
        """
        text = item.text()  # Nombre del archivo seleccionado
        self.label.setText("Archivo seleccionado: " + text)


# Se crea la instancia de la aplicación
app = QtWidgets.QApplication(sys.argv)
# Se crea la instancia de la ventana
miVentana = Ventana()
# Se muestra la ventana
miVentana.show()
# Se entrega el control al sistema operativo
sys.exit(app.exec_())
