from PySide6.QtCore import Qt
from PySide6.QtGui import (QFont, QAction)
from PySide6.QtWidgets import ( QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QMainWindow )
from qdarktheme import load_stylesheet


app = QApplication()
base = QWidget()
layouth = QHBoxLayout()
mainWindow = QMainWindow()

base.setLayout(layouth)
mainWindow.setCentralWidget(base)

mainWindow.show()

app.exec()