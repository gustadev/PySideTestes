from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
import pyqtgraph as pg

application = QApplication()

hora1 = [1,2,3,4,5,6,7,8,9,10]
hora2 = [1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10]
temperatura1 = [30,32,34,32,33,31,29,32,35,45]
temperatura2 = [30,5,34,32,10,31,29,32,35,20]

linha1 = pg.mkPen(color=(255,0,0),width=10)
linha2 = pg.mkPen(color=(0,0,255),width=5)
linha3 = pg.mkPen(color=(0,255,0),width=2)

grafico = pg.PlotWidget()
grafico.plotItem.plot(hora1,temperatura1,pen=linha1)
grafico.plotItem.plot(hora2,temperatura2,pen=linha2)
grafico.plotItem.plot(hora2,temperatura1,pen=linha3)
grafico.setBackground('w')


mainWindow = QMainWindow()
mainWindow.setCentralWidget(grafico)

mainWindow.show()

application.exec()